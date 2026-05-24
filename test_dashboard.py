from nicegui import ui

# ════════════════════════════════════════════════════════════════
# CALCULATOR IMPORTS 
# (Keep these commented out until we translate them to NiceGUI)
# ════════════════════════════════════════════════════════════════
# import calculators.OffPricesCalculator as OffPricesCalculator
# import calculators.SurebetCalculator as SurebetCalculator
# import calculators.TopPriceBetfairCalculator as TopPriceBetfairCalculator
# import calculators.MarginsRemoval as MarginsRemoval
# import calculators.AlternativeLinesConverter as AlternativeLinesConverter
# import calculators.PercentageCalculations as PercentageCalculations
# import calculators.CurrencyConverter as CurrencyConverter 
# import calculators.GeneralTab2 as GeneralTab2
# import calculators.TimeCalculator as TimeCalculator

def create_dashboard():
    # 1. Sleek Top Header
    with ui.header().classes('bg-slate-900 text-white items-center justify-between px-6 py-4 shadow-lg'):
        ui.label('⚡ Pro Betting Tools Dashboard').classes('text-2xl font-bold tracking-wide')
    
    # 2. Main Layout Structure (No wrapping so the sidebar stays fixed)
    with ui.row().classes('w-full h-screen no-wrap'):
        
        # Professional Left Sidebar using Vertical Tabs
        with ui.column().classes('w-64 bg-slate-50 h-full p-4 border-r border-gray-200 shadow-sm shrink-0'):
            ui.label('TOOLS MENU').classes('text-xs font-bold text-gray-500 tracking-widest mb-4')
            
            with ui.tabs().classes('w-full items-start').props('vertical') as tabs:
                tab_off_prices = ui.tab('Off Prices Calculator')
                tab_surebet = ui.tab('Surebet Calculator')
                tab_top_price = ui.tab('Top Price / Betfair')
                tab_margins = ui.tab('Margins Removal')
                tab_alt_lines = ui.tab('Alternative Lines Converter')
                tab_percentage = ui.tab('Percentage (%) Calculations')
                tab_currency = ui.tab('Currency Converter')
                tab_time = ui.tab('Current Time Calculator')
                tab_general = ui.tab('General Tab 2')
                
        # Main Display Panel (Scrollable content area for the active calculator)
        with ui.column().classes('flex-grow p-8 bg-white h-full overflow-y-auto'):
            
            with ui.tab_panels(tabs, value=tab_off_prices).classes('w-full h-full'):
                
                with ui.tab_panel(tab_off_prices):
                    ui.label('Off Prices Calculator').classes('text-3xl font-bold text-slate-800 mb-6')
                    ui.label('Awaiting UI translation...').classes('text-gray-500 italic')
                    # OffPricesCalculator.run()
                    
                with ui.tab_panel(tab_surebet):
                    ui.label('Surebet Calculator').classes('text-3xl font-bold text-slate-800 mb-6')
                    ui.label('Awaiting UI translation...').classes('text-gray-500 italic')
                    # SurebetCalculator.run()
                    
                with ui.tab_panel(tab_top_price):
                    ui.label('Top Price / Betfair Calculator').classes('text-3xl font-bold text-slate-800 mb-6')
                    ui.label('Awaiting UI translation...').classes('text-gray-500 italic')
                    # TopPriceBetfairCalculator.run()
                    
                with ui.tab_panel(tab_margins):
                    ui.label('Margins Removal').classes('text-3xl font-bold text-slate-800 mb-6')
                    ui.label('Awaiting UI translation...').classes('text-gray-500 italic')
                    # MarginsRemoval.run()

                with ui.tab_panel(tab_alt_lines):
                    ui.label('Alternative Lines Converter').classes('text-3xl font-bold text-slate-800 mb-6')
                    ui.label('Awaiting UI translation...').classes('text-gray-500 italic')
                    # AlternativeLinesConverter.run()

                with ui.tab_panel(tab_percentage):
                    ui.label('Percentage (%) Calculations').classes('text-3xl font-bold text-slate-800 mb-6')
                    ui.label('Awaiting UI translation...').classes('text-gray-500 italic')
                    # PercentageCalculations.run()
                    
                with ui.tab_panel(tab_currency):
                    ui.label('Currency Converter').classes('text-3xl font-bold text-slate-800 mb-6')
                    ui.label('Awaiting UI translation...').classes('text-gray-500 italic')
                    # CurrencyConverter.run()

                with ui.tab_panel(tab_time):
                    ui.label('Current Time Calculator').classes('text-3xl font-bold text-slate-800 mb-6')
                    ui.label('Awaiting UI translation...').classes('text-gray-500 italic')
                    # TimeCalculator.run()

                with ui.tab_panel(tab_general):
                    ui.label('General Tab 2').classes('text-3xl font-bold text-slate-800 mb-6')
                    ui.label('Awaiting UI translation...').classes('text-gray-500 italic')
                    # GeneralTab2.run()

# Initialize the interface
create_dashboard()

# Render deployment setup (Host 0.0.0.0 and Port 8080 are required for Render)
ui.run(title="Betting Tools Dashboard", port=8080, host="0.0.0.0")
