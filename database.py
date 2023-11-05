from neo4j import GraphDatabase

driver = GraphDatabase.driver("neo4j+s://9dc6aeb2.databases.neo4j.io", auth=("neo4j", "Y1vnvkYOLBy-uAOYPaQAlixuQfa5I4gNH1yAdZ5pKK8"))

def db_session():
    """Generate a database session."""
    return driver.session()

def close_db():
    """Close the database driver."""
    driver.close()