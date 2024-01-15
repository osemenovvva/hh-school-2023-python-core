from datetime import datetime

class Beer:
    def __init__(self, title=None, production_date=None) -> None:
        self.title = title
        self.production_date = datetime.strptime(production_date, "%d.%m.%Y") if production_date is not None else None
