from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1 style="text-align:center; color:green;">🚀 Flask App Deployed with Terraform 🚀</h1>
    <p style="text-align:center;">This EC2 instance, VPC, subnet, and security group were all provisioned using <b>Terraform</b>.</p>
    <p style="text-align:center;">If you are seeing this page, your Terraform + AWS setup is working perfectly! 🎉</p>
    """

@app.route("/about")
def about():
    return """
    <h2>About this Project</h2>
    <ul>
      <li><b>Infrastructure as Code</b> using Terraform</li>
      <li><b>AWS EC2</b> instance running Ubuntu</li>
      <li><b>Flask</b> app served on port 80</li>
      <li>Provisioners used to copy & run this file automatically</li>
    </ul>
    """

if __name__ == "__main__":
    # Run Flask on port 80 so it’s accessible via EC2 public IP
    app.run(host="0.0.0.0", port=80)
