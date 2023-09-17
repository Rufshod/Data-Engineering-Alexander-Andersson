## Deploying Our Product Through Azure

We've chosen Azure, specifically portal.azure.com, to deploy our product.
Its main benefits over competitors like AWS are its easy to learn UI and automated infrastructure. This allows us to focus more on coding and less on managing the cloud.

Below, I list the Azure resources we'll use for our different scripts and functions, along with the reasons for choosing them.
### Azure Container Registry (ACR)

- We will store our Docker images for our Python scripts and React app. 
- Because we already have our code in GitHub we only need to set up a new GitHub Action to push our scripts to ACR.
- Some examples of the scripts stored in our Docker images are the web scraper, RSS downloader, article extractor, and summarizer.

### Azure Container Instances (ACI)
- After pushing our Docker images to the ACR, we will be using ACI to run our containers. It allows us to run our containers without having to manage any underlying infrastructure, which helps us in our focus on development

### Azure App Services

- Azure App Services enables us to run our React app and the interactive bot continuously. It will automatically scale to meet demand when we go into production.

### Azure Functions

- Most of our smaller, less resource intensive functions. Like our second bot, the summary bot. This bot only runs at the end of our pipeline, posting once all data has been scraped, downloaded, and summarized.
- Because Azure Functions are event driven, it only runs when we need it to, which helps us to keep it cost effective. 

### Azure SQL Database for PostgreSQL

- We're using a PostgreSQL database, making this service a perfect fit for our product. It easily communicates with our Python scripts, React app, and the interactive bot through direct database queries using SQLAlchemy.
- Azure SQL Database also helps us with automated backups and future scaling.

### Azure Key Vault

- This will store our sensitive data, like API-KEY and database login credentials. As we acquire more sensitive user data, this resource will become increasingly useful. Azure Key Vault also sports many security features we are interested in, like audit logs to see when and why our key vault were accessed.
