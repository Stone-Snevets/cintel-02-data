# Imports
import palmerpenguins as pp
import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly

# Load PalmerPenguins into a Dataframe
penguins_df = pp.load_penguins()

# Generate UI
ui.page_opts(title="Stevens: Penguin Data", fillable=True)
with ui.layout_columns():

    # Histogram of Tip
    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    # Histogram of Total Bill
    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
