class CompoundInterest:
    def __init__(
        self,
        principal: float,
        annual_rate: float,
        time: float,
        time_unit: str,  # "anos" ou "meses"
        monthly_contribution: float
    ):
        self.principal = principal
        self.annual_rate = annual_rate
        self.time = time
        self.time_unit = time_unit
        self.monthly_contribution = monthly_contribution

    def calculate_monthly_details(self) -> tuple[float, list]:
        if self.time_unit == "anos":
            months = int(self.time * 12)
        else:
            months = int(self.time)

        monthly_rate = self.annual_rate / 12
        current_balance = self.principal
        total_invested = self.principal 
        total_interest = 0.0
        monthly_data = []

        # Primeiro mês (sem aporte)
        monthly_interest = current_balance * monthly_rate
        total_interest += monthly_interest
        current_balance += monthly_interest
        monthly_data.append({
            "Mês": 1,
            "Juros (R$)": monthly_interest,
            "Total Investido (R$)": total_invested,
            "Total Juros (R$)": total_interest,
            "Total Acumulado (R$)": current_balance
        })

        # Meses seguintes (com aporte)
        for month in range(2, months + 1):
            current_balance += self.monthly_contribution
            total_invested += self.monthly_contribution

            monthly_interest = current_balance * monthly_rate
            total_interest += monthly_interest
            current_balance += monthly_interest

            monthly_data.append({
                "Mês": month,
                "Juros (R$)": monthly_interest,
                "Total Investido (R$)": total_invested,
                "Total Juros (R$)": total_interest,
                "Total Acumulado (R$)": current_balance
            })

        return round(current_balance, 2), monthly_data