CREATE
(dagmawi: PERSON {name: "Dagmawi", age: "22"}),

(python: SKILL {name: "Python", since: "2021"}),
(javascript: SKILL {name: "JavaScript", since: "2022"}),
(typescript: SKILL {name: "TypeScript", since: "2022"}),
(java: SKILL {name: "Java", since: "2022"}),
(bootstrap: SKILL {name: "Bootstrap", since: "2022"}),
(tailwind: SKILL {name: "Tailwind", since: "2023"}),
(htmlcss: SKILL {name: "HTML/CSS", since: "2023"}),
(dart: SKILL {name: "Dart", since: "2023"}),
(flutter: SKILL {name: "Flutter", since: "2023"}),
(datastructures: SKILL {name: "DataStructuresandAlgorithms", since: "2023"}),
(mysql: SKILL {name: "MySQL", since: "2022"}),
(postgresql: SKILL {name: "PostgreSQL", since: "2023"}),
(reactJs: SKILL {name: "ReactJs", since: "2022"}),
(nestJs: SKILL {name: "NestJs", since: "2022"}),
(dotnet: SKILL {name: ".NET", since: "2023"}),
(angular: SKILL {name: "AngularJs", since: "2024"}),
(machineLearning: SKILL {name: "MachineLearning", since: "2023"}),

(aau: EDUCATION {degree: "BSc in Software Engineering", institution: "Addis Ababa University", startyear: "2021", endYear: "2025"}),
(a2sv: EDUCATION {degree: "None", institution: "A2SV", startYear: "2023", endYear: "2024"}),

(prj1: PROJECT {name: "E-commerce web app", description: "Worked on an ecommerce website as part of a class project, which allows people to sell and buy laptops
 online. Implemented the backend end using NestJs, a framework of NodeJs. Took part in implementing a responsive web design."}),
(prj2: PROJECT {name: "Parking Spot Reservation Mobile App", description: "Crafted a user friendly mobile app which allows users to easily book parking spots and owners to upload and
 manage their parking spots. Worked as both a frontend and backend developer. The app is built using the flutter framework using the DDD design principle and uses NestJs for the backend."}),
(prj3: PROJECT {name: "HomeRental System Web app", description: "ERental System Web app Collaborated with teammates in a home rental system web app as part of course final project that lets
 homeowners upload their houses and users to rent houses online. Developed with React for the frontend and NestJs for the backend."}),
(prj4: PROJECT {name: "GeezToAmharicTranslator", description: "Worked on a mobile app that lets users to easly convert from Geez to Amharic both local languages, the project was done using the transformer model
which is based on multi-head attention mechanism."}),

(exp1: EXPERIENCE {title: "FrontEnd Developer", company: "Psyann Graphics", startYear: "2023", endYear: "2024"}),
(exp2: EXPERIENCE {title: "Software Engineer Intern", company: "Addis Ababa Institute of Technology(AAiT)", startYear: "2024", endYear: "2024"}),

(dagmawi)-[:EDUCATED_AT]->(aau),
(dagmawi)-[:EDUCATED_AT]->(a2sv),

(dagmawi)-[:WORKED_AT]->(exp1),
(dagmawi)-[:WORKED_AT]->(exp2),

(dagmawi)-[:HAS_SKILL]->(python),
(dagmawi)-[:HAS_SKILL]->(javascript),
(dagmawi)-[:HAS_SKILL]->(bootstrap),
(dagmawi)-[:HAS_SKILL]->(tailwind),
(dagmawi)-[:HAS_SKILL]->(htmlcss),
(dagmawi)-[:HAS_SKILL]->(dart),
(dagmawi)-[:HAS_SKILL]->(flutter),
(dagmawi)-[:HAS_SKILL]->(datastructures),
(dagmawi)-[:HAS_SKILL]->(mysql),
(dagmawi)-[:HAS_SKILL]->(postgresql),
(dagmawi)-[:HAS_SKILL]->(reactJs),
(dagmawi)-[:HAS_SKILL]->(nestJs),
(dagmawi)-[:HAS_SKILL]->(dotnet),
(dagmawi)-[:HAS_SKILL]->(angular),
(dagmawi)-[:HAS_SKILL]->(machineLearning),

(dagmawi)-[:COMPLETED]->(prj1),
(dagmawi)-[:COMPLETED]->(prj2),
(dagmawi)-[:COMPLETED]->(prj3),
(dagmawi)-[:COMPLETED]->(prj4),

(prj1)-[:USED_SKILL]->(htmlcss),
(prj1)-[:USED_SKILL]->(javascript),
(prj1)-[:USED_SKILL]->(bootstrap),
(prj1)-[:USED_SKILL]->(mysql),
(prj1)-[:USED_SKILL]->(nestJs),

(prj2)-[:USED_SKILL]->(dart),
(prj2)-[:USED_SKILL]->(flutter),
(prj2)-[:USED_SKILL]->(mysql),
(prj2)-[:USED_SKILL]->(nestJs),

(prj3)-[:USED_SKILL]->(htmlcss),
(prj3)-[:USED_SKILL]->(javascript),
(prj3)-[:USED_SKILL]->(tailwind),
(prj3)-[:USED_SKILL]->(mysql),
(prj3)-[:USED_SKILL]->(nestJs),

(prj4)-[:USED_SKILL]->(dart),
(prj4)-[:USED_SKILL]->(flutter),
(prj4)-[:USED_SKILL]->(machineLearning),
(prj4)-[:USED_SKILL]->(datastructures),
(prj4)-[:USED_SKILL]->(python),

(exp1)-[:USED_SKILL]->(reactJs),
(exp1)-[:USED_SKILL]->(htmlcss),
(exp1)-[:USED_SKILL]->(javascript),
(exp1)-[:USED_SKILL]->(typescript),
(exp1)-[:USED_SKILL]->(tailwind),
(exp1)-[:USED_SKILL]->(postgresql),

(exp2)-[:USED_SKILL]->(angular),
(exp2)-[:USED_SKILL]->(htmlcss),
(exp2)-[:USED_SKILL]->(dotnet),
(exp2)-[:USED_SKILL]->(datastructures),
(exp2)-[:USED_SKILL]->(postgresql);