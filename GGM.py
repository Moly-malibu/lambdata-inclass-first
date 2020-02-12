#Gordon Growth Model: Present Value Stocks series of future price per share.
import pandas

#Create Df with abbrevs Columns:
def add_state_name(my_df):
    """Param my_df pandas dataframe with column name "abbrevs"""
    names_map = {
        "EPS":  "earnings per share", 
        "DPR":  "dividend payout ratio", 
        "RR":   "retention rate", 
        "ROE":  "return on equity", 
        "DIV0": "dividend per share at t=0", 
        "g":    "growth Rate", 
        "DIV1": "dividend per share at t=1"'
        "PV":   "present value"
    }
    breakpoint()
    my_col = self.df["abbrevs"]
    other_col = my_col.map(names_map)
    self.df["state_name"] = other_col

if __name__ == "__main__"
    df = pandas.DataFrame({"abbrevs": ["EPS", "DPR", "RR", "ROE", "DIV0", "g", "DIV1", "PV"]})
    print(type(df))
    print(df.head())

#Class definition and transformer:
class DataFrameTransformer(object):
    def __init__(self, df):
        self.df = df
    def inspect_data(self):
        print(self.df.head())

class dividend(share):
    def __init__(self, EPS, ratio):
        # todo: Dividend per share $, Earnings per share(EPS)$, compute the Dividend/Payout Ratio(DPR)%
        self.EPS = EPS
        self.DPR = DPR    @property
    def value_stock(self):
        return f"{self.EPS:,.0f} {self.DPR:,.0f}"    def payout_ratio(self):
        print(f"DPR% {self.EPS.upper()} Percentage!")    @staticmethod
    def __init__(self, payout_ratio, retention_rate):
        # todo: Multiply 100% dividend payour ratio(DPR), compute the Retention Rate(RR).
        self.DPR = DPR
        self.RR = RR    @property
    def retention_rate(self):
        return f"{self.DPR:,.0f} {self.RR:,.0f}"    def payout_ratio(self):
        print(f"RR% {self.retention_rate.upper()} Percentage!")    @staticmethod
    def __init__(self, return_Equity, retention_rate):
        # todo: Multiply 25% Return on Equity(ROE), Retention_Rate(RR), Compute the Growth Rate(g).
        self.ROE = ROE
        self.RR = RR    @property
    def growth_rate(self):
        return f"{self.ROE:,.0f} {self.RR:,.0f}"    def growth_rate(self):
        print(f"g {self.growth_rate.upper()} Percentage!")    @staticmethod
    def __init__(self, Dividend_per_share, growth_rate):
        # todo: Dividend per share at t=0, Growth_rate(g), compute the dividend per share at t=1(Div1).
        #DIV0*(1+g).
        self.DIV0 = DIV0
        self.g = g    @property
    def DIV0(self):
        return f"{self.DIV0:,.0f} {self.g:,.0f}"    def dividend_per_share_at_t_1(self):
        print(f"g {self.DIV0.upper()} Dividend per share at 1 (DIV1)!")    @staticmethod
       def __init__(self, dividend_per_share, Rate_Return):
        # todo: Dividend per share at t=1, Rate Return, growth rate(g), compute the value of the Company's Stock at t=0(PV).
        #DIV1/(RR-g).
        self.DIV1 = DIV1
        self.rate_return = rate_return    
        self.growth_rate = growth_rate   @property
    def DIV1(self):
        return f"{self.DIV1:,.0f} {self.rate_return:,.0f} {self.growth_rate} {self.pv}"  def present_value(self):
        print(f"g {self.rate_return.upper()} COMPUTE THE VALUE OF THE COMPANY'S STOCK AT T=0 (PV)!")    @staticmethod
    def Value_Company_stock():
        print(f"DIVIDEND VALUE!") class PV(share):
    def __init__(self, earnings, ratio, PV):
        super().__init__(earnings, ratio)
        self.starting_center = PV    def PV(self):
        print(f"CALCULATION DIVIDEND PER SHARE & PRESENT VALUE {self.earnings.upper()} Company's Dividend: 
        {self.starting_center}!")if __name__ == "__main__":    
        dividend_share = ratio(earnings="DIVIDEND PER SHARE", rate="%", center="PV")

        transformer = DataFrameTransformer(df)
        transformer.inspect_data()
            df2 = add_state_name(df)
             print(df2.head)
        transformer.add_state_name()
        transformer.inspect_data()


