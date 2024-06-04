from neo4j import GraphDatabase


URI = "neo4j+s://5de91f4b.databases.neo4j.io"
USERNAME = "neo4j"


class DbLayer:
    def __init__(self):
        self.driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

    def run_query(self, query, parameters=None):
        with self.driver.session() as session:
            results = session.run(query, parameters)
            return [dict(record) for record in results]
    

    def register_user(self, name, age, location=None, interests=None):
        query = """
            CREATE (user:USER {name:$name, age: $age, location: $location, interests: $interests})
            RETURN user
            """
        parameters = {
            "name": name, 
            "age": age, 
            "location": location,
            "interests": interests
            }
        

        result = self.run_query(query, parameters)
        return result[0]['user']._properties

    def update_user(self, name=None,  age=None, location=None, interests=None):
        query = """
            MATCH (u:USER {name: $name, age: $age, location: $location, interests: $interests})
            RETURN u
            """
        parameters = {
            "name": name, 
            "age": age, 
            "location": location,
            "interests": interests
            }
        
        result = self.run_query(query, parameters)
        return result[0]['user']._properties
    
    def get_all_users(self):
        query = """
        MATCH (user: USER)
        RETURN (user)
        """
        result = self.run_query(query)
        allUsers = []
        for i in range(len(result)):
            allUsers.append(result[i]['user']._properties)

        return allUsers

    def create_post(self, title, detail=""):
        query = """
            CREATE (post: POST {title: $title, detail: $detail})
            RETURN post
            """
        parameters = {
            "title": title,
            "detail": detail
        }

        result = self.run_query(query, parameters)
        return result

    def like_post(self, user_name, post_title):
        query = """
            MATCH (user: USER {name: $user_name}), (post: POST {title: $post_title})
            CREATE (user)-[:LIKES]->(post)
            RETURN user, post
            """
        parameters = {
            "user_name": user_name,
            "post_title": post_title
        }
        result = self.run_query(query, parameters)

        return result

    def comment_on_post(self, user_name, post_title, comment=""):
        query = """
            MATCH (user: USER {name: $user_name}), (post: POST {title: $post_title})
            CREATE (user)-[r:COMMENTED_ON {text: $comment}]->(post)
            RETURN user, post
            """
        parameters = {
            "user_name": user_name,
            "post_title": post_title,
            "comment": comment
        }
        result = self.run_query(query, parameters)

        return result

    def accept_request(self, name1, name2):
        query = """
            MATCH (user1: USER {name: $name1}), (user2: USER {name: $name2})
            CREATE (user1)-[r1:FRIENDS_WITH]->(user2)
            CREATE (user1)<-[r2:FRIENDS_WITH]-(user2)
            return r1, r2
            """
        
        parameters = {
            "name1": name1,
            "name2": name2
        }
        
        result = self.run_query(query, parameters)
    
        return []

    def unfriend(self, name1, name2):
        query = """
            MATCH (user1: USER {name: $name1})-[f:FRIENDS_WITH]->(user2: USER {name: $name2}), 
            (user1: USER {name: $name1})<-[f2:FRIENDS_WITH]-(user2: USER {name: $name2})
            DELETE f, f2
            """
        
        parameters1 = {
            "name1": name1,
            "name2": name2
        }

        parameters2 = {
            "name1": name2,
            "name2": name1
        }
        
        result1 = self.run_query(query, parameters1)
        result2 = self.run_query(query, parameters2)
        return []

    def create_group(self, name):
        query = """
            CREATE (group: GROUP {name: $name, members: 1})
            RETURN group
                """
        
        parameters = {
            "name": name
        }

        result = self.run_query(query, parameters)
        return result

    def join_group(self, user_name, group_name):
        query = """
            MATCH (user: USER {name: $user_name}), (group: GROUP {name: $group_name})
            CREATE (user)-[:IS_MEMBER_OF]->(group)
            RETURN user, group
                """
        parameters = {
            "user_name": user_name,
            "group_name": group_name
        }
        
        result = self.run_query(query, parameters)

        return result


    def send_friend_request(self, sender_name, receiver_name):
        query = """
            MATCH (user1: USER {name: $sender_name}), (user2: USER {name: $receiver_name})
            CREATE (user1)-[r1: OUTGOING_REQUEST]->(user2), (user2)-[r2: INCOMING_REQUEST]->(user1)
            RETURN user1, user2
            """
        
        parameters = {
            "sender_name": sender_name,
            "receiver_name": receiver_name
        }

        result = self.run_query(query, parameters)

        return result
    
    def see_incoming_requests(self, name):
        query = """
            MATCH (user1: USER {name: $name})<-[:INCOMING_REQUEST]-(user:  USER)
            RETURN user
            """
        parameters = {
            "name": name
        }

        result = self.run_query(query, parameters)
        allRequestedUsers = []
        for i in range(len(result)):
            allRequestedUsers.append(result[i]['user']._properties)

        return allRequestedUsers
    
    def find_user_by_name(self, name):
        query = """
            MATCH (user: USER {name: $name})
            RETURN user
            """
        parameters = {
            "name": name
        }

        result = self.run_query(query, parameters)
        print(result)
        
        return result[0]['user']._properties
    
    


