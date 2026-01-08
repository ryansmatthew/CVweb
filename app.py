from flask import Flask, render_template

app = Flask(__name__)

DATA = {
    "name": "Nguyen Duy Tuan Anh",
    "title": "Information Technology (IT) — IT Support / Infrastructure",
    "contact": {
        "phone": "(84) 377-182-906",
        "email": "politysimple@gmail.com",
    },
    "profile": (
        "As an IT Support Specialist, I provide fast technical support to ensure stable and secure "
        "system operations. With broad expertise in hardware, software, and strong communication "
        "skills, I deliver efficient solutions for users."
    ),
    "experience": [
        {
            "role": "IT Support and Infrastructure Specialist",
            "company": "CONG TY TNHH MTV LANCHI BUSINESS",
            "time": "06-2018 to 03-2022",
            "location": "Khu Vai Coi - Trung Son Tram - Son Tay - Ha Noi",
            "details": [
                "Supported end users/clients; deployed new IT systems for supermarkets.",
                "Maintained SQL, VMware, Domain Controller, Cisco, ERP, Fortigate.",
                "Built automation tools (PowerShell, batch scripts, Python).",
                "Monitored batch jobs with self-built PRTG/Zabbix to ensure stability.",
            ],
        },
        {
            "role": "IT Support Specialist",
            "company": "VNT Logistics (CONG TY CTCP GIAO NHAN VAN TAI NGOAI THUONG)",
            "time": "03-2022 to 02-2023",
            "location": "Bich Cau, Quoc Tu Giam, Dong Da, Ha Noi",
            "details": [
                "End-user/client support; maintained VMware, Domain Controller, app servers, core switches.",
                "Managed FAST application (user creation/access control) and IT policies.",
                "Server build/rebuild; improved HA for servers/network; managed Office 365.",
                "Managed FTTH service contracts and web hosting.",
            ],
        },
        {
            "role": "IT Support Specialist and IT Operator",
            "company": "Central Retail in Vietnam",
            "time": "03-2023 to Present",
            "location": "163 D. Phan Đang Luu, Phuong 1, Phu Nhuan, HCM",
            "details": [
                "Handled ServiceDeskPlus tasks: network, POS (Vynamic/Dynamic AX), client-server, onboarding/offboarding.",
                "Supported SharePoint, IP phones, in-house apps; supported new store opening/renovation.",
                "Installed POS; configured Dynamic AX; set up networks (Cisco, Huawei, Aruba).",
                "Operator: monitored/troubleshot network systems; oversaw batch jobs, reruns, notifications.",
                "Built Python tool for monthly attribute manager updates; documented issues into SOPs.",
            ],
        },
    ],
    "education": [
        {"name": "Trung Cap Bach Khoa", "detail": "Trung Cap CNTT", "date": "2021 - 2023"},
        {"name": "CCNA", "detail": "ID NO. CSCO14423725", "date": "July 26, 2023"},
        {"name": "FCAC", "detail": "2254673881NT", "date": "October 4, 2023"},
    ],
    "skills": [
        "Network Troubleshooting and Support",
        "POS System Management",
        "Client-Server Troubleshooting",
        "Onboarding and Offboarding Support",
        "SharePoint and IP Phone Support",
        "In-House Application Support",
        "IT Infrastructure Setup",
        "System Monitoring and Issue Resolution",
        "Batch Job Management (PRTG, Zabbix)",
        "Automation and Tool Development (Python, PowerShell, Batch scripts)",
        "Hardware and Infrastructure Provisioning",
        "High Availability (HA) for Servers and Networks",
        "Office 365 Management",
        "Contract Management (FTTH, web hosting)",
        "SOP Creation and Documentation",
    ],
    "interests": [
        "Developing automation tools and improving operational efficiency",
        "Enhancing IT infrastructure and system stability",
        "Implementing HA solutions for critical systems",
        "Streamlining support processes for end users and clients",
        "Learning new technologies and troubleshooting techniques",
        "Building SOPs to standardize workflows and reduce operational errors",
    ],
}

DATA.update({
    "headline": "Experienced IT Support Specialist | 7 Years in Retail | Technical Solutions & Problem Solving",
    "location": "Ho Chi Minh City Metropolitan Area",
    "connections": "500+ connections",
    "company": "Central Retail in Vietnam",
    "school": "Trường Trung Cấp Bách Khoa",
    "cta": [
        {"label": "Đang tìm", "href": "#contact", "primary": True},
        {"label": "Phần Thêm hồ sơ", "href": "#profile", "primary": False},
        {"label": "Cải thiện hồ sơ", "href": "#experience", "primary": False},
        {"label": "Tài nguyên", "href": "#skills", "primary": False},
    ],
    "images": {
        "cover": "img/cover.jpg",
        "avatar": "img/avatar.jpg",
    }
})


@app.get("/")
def home():
    return render_template("index.html", data=DATA)

if __name__ == "__main__":
    app.run(debug=True)
