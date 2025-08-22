# DevSecOps for a Microservices Application  

## 📌 Overview  
This repository contains the **documentation** for our project **DevSecOps for a Microservices App**, created as part of the **Post Graduate Diploma in IT Infrastructure, Systems, and Security (PG-DITISS) at C-DAC, Pune**.  

The project demonstrates how to implement a **DevSecOps pipeline** for deploying Python-based microservices with a focus on security, automation, and scalability.  

---

## 📖 Documentation  
The complete project report is available here:  

📄 [Project Documentation (PDF)](./docs/DevSecOps_Documentation.pdf)  

---

## 🚀 Project Highlights  
- **Python-based microservices** with Docker containerization  
- **CI/CD Pipeline** with Jenkins, GitHub, and AWS EKS  
- **Security Integration**  
  - Static code analysis (SonarQube)  
  - Vulnerability scanning (Trivy, OWASP Dependency Check, Docker Scout)  
- **Cloud & Orchestration**  
  - AWS EC2, IAM, and EKS  
  - Kubernetes deployments with Helm  
- **Monitoring & Observability**  
  - Prometheus for metrics  
  - Grafana dashboards  

---

## 🎯 Future Scope  
- Integrating advanced runtime security (Aqua Security, Anchore)  
- Multi-cloud deployment (Azure AKS, Google GKE)  
- Infrastructure as Code (Terraform, CloudFormation)  
- Service Mesh (Istio, Linkerd) for microservices traffic management  

---

## 📂 Repository Structure  
devsecops-microservice-project/
│
├── microservice/              # Python microservice app
│   ├── src/                   # Application source code
│   │   └── app.py
│   ├── tests/                 # Unit tests
│   │   └── test_app.py
│   ├── requirements.txt       # Dependencies
│   ├── Dockerfile             # Containerization
│   └── README.md              # App-specific notes
│
├── ci-cd/                     # CI/CD pipelines
│   ├── Jenkinsfile
│   └── github-actions.yml
│
├── security/                  # Security configs & reports
│   ├── sonar-project.properties
│   ├── trivy-scan.sh
│   └── reports/
│       ├── trivy-fs-report.txt
│       ├── trivy-image-report.txt
│       └── sonar-report.json
│
├── eks/                       # AWS EKS deployment manifests
│   ├── deployment.yaml        # App deployment on EKS
│   ├── service.yaml           # Service definition for EKS
│   ├── ingress.yaml           # Ingress rules 
│   └── eksctl-config.yaml     # eksctl cluster config
│
├── docs/                      # Project documentation
│   └── Project_DevSecOps.pdf
│
├── README.md                  # Project overview

