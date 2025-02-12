from entities.compound_interest import CompoundInterest

class CalculateCompoundInterestUseCase:
    def execute(
        self,
        principal: float,
        annual_rate: float,
        time: float,
        time_unit: str,
        monthly_contribution: float
    ) -> tuple[float, list]:
        calculator = CompoundInterest(
            principal, annual_rate, time, time_unit, monthly_contribution
        )
        return calculator.calculate_monthly_details()