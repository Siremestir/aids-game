class Protagonist:
    def __init__(self,
                ethics:int,
                research:int,
                credibility:int,
                finance:int):
        self._ethics = ethics
        self._research = research
        self._credibility = credibility
        self._finance = finance
        return self
    

    def get_ethics(self) -> int:
        return self._ethics

    
    def set_ethics(self, ethics:int) -> None:
        self._ethics = ethics

    
    def get_research(self) -> int:
        return self._research
    

    def set_research(self, research:int) -> None:
        self._research = research

    
    def get_credibility(self) -> int:
        return self._credibility

    
    def set_credibility(self, credibility:int) -> None:
        self._credibility = credibility
    
    
    def get_finance(self) -> int:
        return self._finance
    

    def set_finance(self, finance:int) -> None:
        self._finance = finance