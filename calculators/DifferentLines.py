from typing import Dict, Optional
from dataclasses import dataclass

@dataclass
class OddsResult:
    """
    Stores the calculation results for odds comparison across different lines.
    """
    kaizen_line: float
    kaizen_odds: float
    comp_at_kaizen_line: float
    difference_percentage: float
    status: str

class DifferentLinesCalculator:
    """
    Calculator for analyzing odds differences between Kaizen and competition
    when they have different lines.
    """
    
    def __init__(self):
        # Standard odds increment ladder
        self.INCREMENTS: Dict[float, float] = {
            1.38: 1.40, 1.40: 1.43, 1.43: 1.45, 1.45: 1.47, 1.47: 1.50,
            1.50: 1.52, 1.52: 1.55, 1.55: 1.57, 1.57: 1.62, 1.62: 1.66,
            1.66: 1.71, 1.71: 1.76, 1.76: 1.90, 1.90: 2.00, 2.00: 2.10,
            2.10: 2.20, 2.20: 2.30, 2.30: 2.40, 2.40: 2.50, 2.50: 2.60,
            2.60: 2.70, 2.70: 2.85
        }
        self.REVERSE_INCREMENTS = {v: k for k, v in self.INCREMENTS.items()}

    def _validate_input(self, value: float, name: str) -> None:
        """
        Validates input values for the calculator.
        
        Args:
            value: The value to validate
            name: Name of the value for error messages
        
        Raises:
            ValueError: If the input is invalid
        """
        if value <= 0:
            raise ValueError(f"{name} must be positive")
        if name.endswith('odds') and value < 1:
            raise ValueError(f"{name} must be greater than or equal to 1")

    def _find_nearest_odds(self, odds: float, lookup_dict: Dict[float, float]) -> Optional[float]:
        """
        Finds the nearest valid odds value in the lookup dictionary.
        """
        if odds in lookup_dict:
            return odds
        
        keys = sorted(lookup_dict.keys())
        for i in range(len(keys) - 1):
            if keys[i] <= odds <= keys[i + 1]:
                return keys[i] if abs(odds - keys[i]) < abs(odds - keys[i + 1]) else keys[i + 1]
        return None

    def _step_odds(self, odds: float, step_up: bool = True) -> float:
        """
        Steps odds up or down according to the increment ladder.
        
        Args:
            odds: Current odds value
            step_up: True to step up, False to step down
        
        Returns:
            float: New odds value after stepping
        """
        if step_up:
            nearest = self._find_nearest_odds(odds, self.INCREMENTS)
            return self.INCREMENTS.get(nearest, odds + 0.05)
        else:
            nearest = self._find_nearest_odds(odds, self.REVERSE_INCREMENTS)
            return self.REVERSE_INCREMENTS.get(nearest, odds - 0.05)

    def calculate_competition_odds(self, 
                                kaizen_line: float,
                                kaizen_odds: float,
                                comp_line: float,
                                comp_odds: float) -> float:
        """
        Calculates the competition's odds adjusted to the Kaizen line.
        
        Args:
            kaizen_line: Kaizen's betting line
            kaizen_odds: Kaizen's odds
            comp_line: Competition's line
            comp_odds: Competition's odds
            
        Returns:
            float: Competition's adjusted odds at Kaizen line
        """
        # Validate all inputs
        for name, value in [
            ("Kaizen line", kaizen_line),
            ("Kaizen odds", kaizen_odds),
            ("Competition line", comp_line),
            ("Competition odds", comp_odds)
        ]:
            self._validate_input(value, name)

        line_diff = int(kaizen_line - comp_line)
        current_odds = comp_odds

        # Adjust odds based on line difference
        for _ in range(abs(line_diff)):
            current_odds = self._step_odds(current_odds, line_diff > 0)
            
        return current_odds

    def calculate_difference(self, kaizen_odds: float, comp_odds: float) -> float:
        """
        Calculates the percentage difference between Kaizen and competition odds.
        """
        return ((1 / kaizen_odds) - (1 / comp_odds)) * 100

    def get_status(self, difference: float) -> str:
        """
        Determines the status based on the calculated difference percentage.
        """
        if difference > -2:
            return "OK"
        elif -3 <= difference <= -2:
            return "Off 2"
        else:
            return "Off 1"

    def calculate(self, kaizen_line: float, kaizen_odds: float,
                 comp_line: float, comp_odds: float) -> OddsResult:
        """
        Performs the complete calculation and returns a result object.
        """
        comp_at_kaizen = self.calculate_competition_odds(
            kaizen_line, kaizen_odds, comp_line, comp_odds)
        difference = self.calculate_difference(kaizen_odds, comp_at_kaizen)
        status = self.get_status(difference)
        
        return OddsResult(
            kaizen_line=kaizen_line,
            kaizen_odds=kaizen_odds,
            comp_at_kaizen_line=comp_at_kaizen,
            difference_percentage=difference,
            status=status
        )

def main():
    """
    Main function to run the different lines calculator with command line input.
    """
    calculator = DifferentLinesCalculator()
    
    try:
        # Get user inputs with error handling
        inputs = {}
        prompts = {
            'kaizen_line': "Kaizen line: ",
            'kaizen_odds': "Kaizen odds: ",
            'comp_line': "Competition line: ",
            'comp_odds': "Competition odds: "
        }
        
        for key, prompt in prompts.items():
            while True:
                try:
                    inputs[key] = float(input(prompt))
                    break
                except ValueError:
                    print("Please enter a valid number")
        
        # Calculate results
        result = calculator.calculate(**inputs)
        
        # Display results
        print(f"\nOur Line is ({result.kaizen_line}) at ({result.kaizen_odds}).")
        print(f"Competition on ({result.kaizen_line}) is ({result.comp_at_kaizen_line}).")
        
        # Display status with color coding
        status_colors = {
            "OK": "\033[92m",      # Green
            "Off 2": "\033[95m",   # Purple
            "Off 1": "\033[91m"    # Red
        }
        color = status_colors.get(result.status, "")
        print(f"{color}**We have {result.status}** (difference = {result.difference_percentage:.2f}%)\033[0m")
        
        print("\nDisclaimer: This is an approximated calculator. Real odds may have a small difference.")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
