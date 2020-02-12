# My Lambdata Package

# Installation
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc. Markdown(
            """
            Installation Instructions:
            TODO Gordon Growth Model is P= D1/r-g. 
            where:      P= Current Stock Price.
                        g= Constant growth rate expected for dividends, in perpetuity.
                        r= Constant cost of equity capital for the company(rate of return).
                        D1 = Value of next year's dividends.
            EPS Decreased: Earning by share is decreased by stock dividend.
            DPR: It is the percentage of earnings paid to shareholders in dividends.
            """ 
        ),
    ],    
    md=4,
)

column2 = dbc.Col([html.Img(src='assets/homepage.jpg', className='img-fluid')
],
align='center'
)

layout = dbc.Row([column1, column2])

# Usage

usage Instructions:

TODO