# agent.py

def get_queries_from_llm(date, location):
    """
    Temporary mock LLM planner.
    """
    return ["pumpkin", "ice skating", "farmers market", "swimming"]

def search_events(query, date):
    """
    Mock function to return events.
    """
    return [
        {"name": f"{query} Event 1", "date": date, "location": "Nearby Park"},
        {"name": f"{query} Event 2", "date": date, "location": "Community Center"},
    ]

def filter_kid_friendly(events):
    """
    Mock filter: keep only kid-friendly events
    """
    return [e for e in events if "pumpkin" in e["name"].lower() or "ice skating" in e["name"].lower()]

  
def run_agent(date, location):
    activities = []
    queries = get_queries_from_llm(date, location)
    for q in queries:
        events = search_events(q, date)
        filtered = filter_kid_friendly(events)
        activities.extend(filtered)
    return activities
