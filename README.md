**🚀 **Terraform AWS EC2 + Flask Project****

**Project Overview**
Automate the deployment of an AWS EC2 instance running a Flask web application using Terraform.

**Key Highlights:**

* Infrastructure as Code (IaC)
* VPC, Subnet, Internet Gateway, Route Table setup
* Security Groups (SSH + HTTP)
* Key Pair provisioning for SSH access
* EC2 instance deployment with Flask app

**🛠 Tech Stack**

* Terraform → IaC for AWS resources
* AWS → Cloud provider
* EC2 → Virtual machine
* Flask → Python web framework
* Python 3 & pip → Runtime & dependency management

**📦 Project Structure**

```
terraform-ec2-flask/
│
├─ main.tf              # Terraform code for AWS resources
├─ app.py               # Flask app to deploy
├─ .gitignore           # Ignore sensitive files
├─ README.md            # Project overview
└─ .terraform.lock.hcl  # Terraform provider lock
```

**⚡ Features**

* Fully automated AWS EC2 provisioning
* Flask app deployment via Terraform provisioners
* Security Group rules for SSH and HTTP
* Repeatable Infrastructure as Code workflow

**💻 How to Run**

```
# Clone the repository
git clone https://github.com/<YOUR_USERNAME>/terraform-ec2-flask.git
cd terraform-ec2-flask

# Initialize Terraform
terraform init

# Apply Terraform configuration
terraform apply

# Access the Flask app
http://<EC2_PUBLIC_IP>
```

**⚙ Workflow (Simplified)**

```
Terraform Apply
       ↓
Create VPC, Subnet, IGW, Route Table
       ↓
Create Security Group & Key Pair
       ↓
Launch EC2 Instance
       ↓
Provision EC2 (Copy Flask app, Install Python3, pip, Flask, Run app)
       ↓
Flask App Running → Access via http://<EC2_PUBLIC_IP>
```

**🔐 Security Notes**

* Do not commit private keys (.pem / .key) to GitHub
* Terraform state files contain sensitive information → keep them ignored in .gitignore
