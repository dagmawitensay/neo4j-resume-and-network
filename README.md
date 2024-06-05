# neo4j-resume-and-network

## Overview

This project consists of two main parts:
1. A simple resume represented in a Neo4j graph.
2. A simple social network represented in a Neo4j graph.

## Prerequisites

Before you begin, ensure you have the following installed:
- [Neo4j Desktop](https://neo4j.com/download/)
- [Neo4j Browser](https://neo4j.com/developer/neo4j-browser/)

## Project Structure

### 1. Resume network

#### Nodes
- **Person**: Represents the individual whose resume is being described.
  - Properties: `name`
- **Education**: Represents an educational qualification.
  - Properties: `degree`, `institution`, `year`
- **WorkExperience**: Represents a work experience entry.
  - Properties: `position`, `company`, `startYear`, `endYear`
- **Skill**: Represents a skill.
  - Properties: `name`, `since`

#### Relationships
- `(:Person)-[:EDUCATED_AT]->(:Education)`
- `(:Person)-[:WORKED_AT]->(:WorkExperience)`
- `(:Person)-[:HAS_SKILL]->(:Skill)`

#### Example cypher queries
- Create a Person node:
    ```cypher
    CREATE (person: PERSON {name: "Teshome Mekonen"}),
    (edu: EDUCATION {degree: 'BSc in Software Engineerig', institution: 'Addis Ababa University', startYear: 2020, endYear: 2025}),
    (person)-[:EDUCATED_AT]->(edu)
    ```

### 2. Social netowrk

This part of the project involves creating a Neo4j graph to represent a simple social network. The graph includes nodes and relationships to describe users and their connections (friends).

#### Nodes
- **User**: Represents a user in the social network.
  - Properties: `name`,  `age`,  `location`, `interests`
- **Post**: Represents a user post.
  - Properties: `title`, `detail`

#### Relationships
- `(:User)-[:FRIENDS_WITH]]->(:User)`
- `(:User)-[:LIKES]->(:Post)`

## Getting Started

### For the resume graph
1. Open Neo4j Desktop and create a new project.
2. Create a new database and start it.
3. Open Neo4j Browser.
4. Run the example Cypher queries provided above to create the nodes and relationships for the resume graph.

### For the social network graph
1. Create account and instance on neo4j [AuraDB](https://neo4j.com/cloud/platform/aura-graph-database/)
2. Use the username and password to connected to database.
3. Run the flask server and use the endpoints to create nodes and relationships.