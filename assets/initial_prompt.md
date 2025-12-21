Given is the contents from my resume:
Kaustav Paul

Software Engineer – Full-Stack | Distributed Systems & Microservices | Cloud Technologies
+91-9830843664 | paul.kaustav@outlook.com | LinkedIn | LeetCode | GitHub

Skills
Languages & Scripting: Java, Scala, Python, C++, TypeScript, Bash
Backend Frameworks & Tools: Spring Boot, Akka, Flask, Node.js, Apache Airflow, WebSockets, JWT
Big Data & Distributed Systems: Apache Spark, Hadoop, YARN, Kafka, PubSub, Redis
Database & Data Warehousing: Oracle, PostgreSQL, HDFS, Google Cloud Storage, GCP BigQuery
Cloud Platforms: Google Cloud Platform (GCP), Red Hat OpenShift
DevOps & Infrastructure: Docker, Kubernetes (k8s), Helm, Jenkins, Terraform, Maven, Gradle
Monitoring & Logging: Grafana, Prometheus, Splunk
CS Fundamentals: Data Structures & Algorithms, System Design, OOP, DBMS, OS, Computer Networks
Experience
Deutsche Bank Hybrid
Associate Engineer - Accelerated Promotion Oct 2023 – Present
• Implemented a Redis-based queueing system to replace FIFO YARN scheduling, allowing time sensitive jobs
to be processed first and ensuring that stress run outputs are made available to users with minimal delay
• Designed and developed a high-performance REST API and WebSocket service using Scala, Akka, Java, and
Spring, enabling real-time access to stress run summaries on UI, significantly improving system responsiveness
• Developed a scalable data segregation service using Java, Springboot & Spark to organize trade data by
country, enforcing data governance protocols and enabling compliant cloud migration
• Built a GCP Cloud Composer-based data orchestration solution to automate data transfers from on-prem
HDFS to Google Cloud Storage, reducing operational storage costs by 85% under hybrid architecture rules
• Deployed JupyterHub on GKE using Terraform and GitHub Actions, configured network access to dbLLM APIs,
enabling users to analyze GCP-hosted data using GPU-accelerated notebooks
Deutsche Bank Hybrid
Technology Analyst Jul 2021 – Sep 2023
• Designed and developed a scalable Data Quality Check framework to validate large-scale datasets, using
Java, Springboot & Spark; enabled users to confidently sign off stress-run processes based on data integrity.
• Automated the loading of JIRA, ServiceNow & Incidents data into ADC dashboard using Apache Airflow,
increasing metric update frequency from monthly to daily and improving operational visibility across teams
• Implemented TDD for Stress Testing UI application using Jasmine (unit tests) and Protractor (e2e), achieving
80%+ test coverage for production compliance
SkyBits Technologies Pvt Ltd Kolkata, West Bengal
Fullstack Developer Intern Apr 2020 – Jun 2020
• Engineered a data processing pipeline to clean and transform user-provided business KPIs and SPIs and
designed an intuitive dashboard to improve daily decision-making and enhance stakeholder engagement
• Technologies used: Node.js, MySQL, ETL, React, Chart.js, React Gauge
Itobuz Technologies Pvt Ltd Kolkata, West Bengal
MERN Stack Developer Intern Dec 2019 – Jan 2020
• Developed an automated invoice management system for streamlined operations and integrated a secure
role-based access control (RBAC) system to safeguard sensitive financial data
• Technologies used: MERN stack (MongoDB, Express.js, React, Node.js), JWT authentication
Education
Indian Institute of Engineering Science and Technology, Shibpur Jul 2017 - Jun 2021
BTech in Computer Science and Engineering 8.86/10 CGPA



I need you to read the above resume content and compare against the job_description: {{ $json.job_description }}

Keep a keen eye on the years of experience in the job description. If the required experience is more than 5 years or less 2 years, assign a score 0. Also take into account the graduation date, take the delta against datetime {{ $('Schedule Trigger').item.json['Readable date'] }} to calculate the years of experience.

Output a score and a one liner reasoning behind the score.