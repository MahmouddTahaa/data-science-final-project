import dash
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import sys
from pathlib import Path

sys.path.append(str(Path.cwd() / 'src'))

from utils import processing_utils as pu
from utils import plotting as plot
from utils import eda

app = dash.Dash(
    __name__, 
    external_stylesheets=[dbc.themes.LUX],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
)
server = app.server  

DATA_PATH = Path('data/processed/fordgobike_processed.csv')
try:
    print("⏳ Loading data...")
    df = pu.load_data(str(DATA_PATH))
    print(f"✅ Loaded {len(df):,} rows.")
except Exception as e:
    print(f"❌ Error loading data: {e}")
    df = pd.DataFrame({
        'user_type': ['Subscriber', 'Customer'] * 50,
        'member_gender': ['Male', 'Female', 'Other'] * 33 + ['Male'],
        'duration_minutes': np.random.exponential(10, 100),
        'age': np.random.normal(35, 10, 100).astype(int),
        'bike_share_for_all_trip': ['Yes', 'No'] * 50,
        'member_birth_year': np.random.randint(1950, 2000, 100)
    })


def create_card(title, value, description, color="primary"):
    """Create a KPI card."""
    return dbc.Card(
        dbc.CardBody([
            html.H6(title, className="card-subtitle text-muted mb-2"),
            html.H3(value, className=f"card-title text-{color}"),
            html.P(description, className="card-text small text-muted")
        ]),
        className="mb-4 shadow-sm h-100"
    )

sidebar = html.Div(
    [
        html.H2("🚴 Ford GoBike", className="display-6"),
        html.Hr(),
        html.P("Filter the dashboard:", className="lead"),
        
        html.Label("User Type", className="fw-bold mt-3"),
        dcc.Dropdown(
            id="filter-user-type",
            options=[{'label': i, 'value': i} for i in sorted(df['user_type'].unique())],
            multi=True,
            placeholder="All User Types"
        ),
        
        html.Label("Member Gender", className="fw-bold mt-3"),
        dcc.Dropdown(
            id="filter-gender",
            options=[{'label': i, 'value': i} for i in sorted(df['member_gender'].unique())],
            multi=True,
            placeholder="All Genders"
        ),
        
        html.Label("Bike Share for All", className="fw-bold mt-3"),
        dbc.RadioItems(
            id="filter-program",
            options=[
                {"label": "All", "value": "all"},
                {"label": "Yes", "value": "Yes"},
                {"label": "No", "value": "No"},
            ],
            value="all",
            className="mt-2"
        ),
        
        html.Hr(className="my-4"),
        html.Div([
            html.P("Data Source: Ford GoBike System Data", className="small text-muted"),
            html.P("Final Project - Data Science", className="small text-muted mb-0"),
        ])
    ],
    style={
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "18rem",
        "padding": "2rem 1rem",
        "background-color": "#f8f9fa",
    },
)

content = html.Div(
    id="page-content",
    style={
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    },
)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])

@callback(
    Output("page-content", "children"),
    [
        Input("filter-user-type", "value"),
        Input("filter-gender", "value"),
        Input("filter-program", "value"),
    ]
)
def render_page_content(user_types, genders, program):
    dff = df.copy()
    
    if user_types:
        dff = dff[dff['user_type'].isin(user_types)]
    
    if genders:
        dff = dff[dff['member_gender'].isin(genders)]
        
    if program != 'all':
        dff = dff[dff['bike_share_for_all_trip'] == program]
    
    total_trips = len(dff)
    avg_duration = dff['duration_minutes'].mean()
    avg_age = dff['age'].mean()
    
    kpi_row = dbc.Row([
        dbc.Col(create_card("Total Trips", f"{total_trips:,}", "Filtered trip count"), md=4),
        dbc.Col(create_card("Avg Duration", f"{avg_duration:.1f} min", "Average trip time", "success"), md=4),
        dbc.Col(create_card("Avg User Age", f"{avg_age:.1f} yrs", "Average rider age", "info"), md=4),
    ])
    
    fig_user = plot.plot_categorical_distribution(dff, 'user_type', title="User Type Distribution")
    fig_gender = plot.plot_categorical_distribution(dff, 'member_gender', title="Gender Distribution")
    
    dff_sample = dff.sample(min(5000, len(dff))) if len(dff) > 0 else dff
    
    fig_dur_hist = plot.plot_numeric_distribution(dff, 'duration_minutes', title="Trip Duration Histogram", show_mean=True)
    fig_dur_box = plot.plot_boxplot_by_category(dff, 'duration_minutes', 'user_type', title="Duration by User Type")

    fig_age_dist = plot.plot_age_distribution_with_outliers(dff, title="Age Distribution")
    fig_age_violin = plot.plot_violin_by_category(dff, 'age', 'member_gender', title="Age by Gender")
    
    corr_matrix = eda.compute_correlation_matrix(dff, columns=['age', 'duration_minutes', 'member_birth_year'])
    fig_corr = plot.plot_correlation_heatmap(dff, columns=['age', 'duration_minutes', 'member_birth_year'], title="Correlation Matrix")
    
    tabs = dbc.Tabs([
        dbc.Tab(label="📊 Overview", children=[
            html.Br(),
            dbc.Row([
                dbc.Col(dcc.Graph(figure=fig_user), md=6),
                dbc.Col(dcc.Graph(figure=fig_gender), md=6),
            ])
        ]),
        
        dbc.Tab(label="⏱️ Trip Analysis", children=[
            html.Br(),
            dbc.Row([
                dbc.Col(dcc.Graph(figure=fig_dur_hist), md=12, className="mb-4"),
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(figure=fig_dur_box), md=12),
            ]),
        ]),
        
        dbc.Tab(label="👥 Demographics", children=[
            html.Br(),
            dbc.Row([
                dbc.Col(dcc.Graph(figure=fig_age_dist), md=12, className="mb-4"),
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(figure=fig_age_violin), md=12),
            ])
        ]),
        
        dbc.Tab(label="📈 Correlations", children=[
            html.Br(),
            dbc.Row([
                dbc.Col(dcc.Graph(figure=fig_corr), md=8, className="mx-auto"),
            ])
        ])
    ])
    
    return html.Div([
        html.H3("Dashboard Overview", className="mb-4"),
        kpi_row,
        html.Hr(),
        tabs
    ])

if __name__ == "__main__":
    print("� Starting Dash App...")
    print("� Open http://127.0.0.1:8050/ in your browser")
    app.run(debug=True, port=8050)
