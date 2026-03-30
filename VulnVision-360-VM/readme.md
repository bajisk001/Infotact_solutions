# 🚀 VulnVision 360 – Continuous Compliance & Threat Exposure Engine

## 📌 Project Overview

**Domain:** Vulnerability Management (VM)
**Objective:**
Continuously identify, prioritize, and remediate vulnerabilities and misconfigurations in legacy systems using automated tools.

---

## 🎯 Problem Statement

Legacy systems were not patched regularly, leading to:

* Exposure to critical CVEs
* Weak configurations
* Non-compliance with CIS Benchmarks

---

## 🛠️ Tools Used

* Nmap – Network Discovery
* OpenVAS (GVM) – Vulnerability Scanning
* OpenSCAP (oscap) – Compliance Checking
* Ubuntu Server – Target System
* Bash / SSH – Remediation

---

## 📅 Execution Flow

### 🔹 Week 1: Asset Discovery

* Performed network scan using Nmap
* Identified live hosts, OS, and open ports

---

### 🔹 Week 2: Vulnerability Assessment

* Ran Unauthenticated Scan (external view)
* Ran Authenticated Scan (internal view)

**Result:**

* Authenticated scan revealed more critical vulnerabilities

---

### 🔹 Week 3: Compliance Automation

* Installed OpenSCAP
* Executed CIS Level 1 compliance scan

---

### 🔹 Week 4: Remediation & Re-Scan

* Disabled root SSH login
* Restarted SSH service
* Re-ran compliance scan

**Result:**

* Improved compliance score
* Reduced security risks

---

## 🔄 Vulnerability Management Lifecycle

1. Discover Assets
2. Scan for Vulnerabilities
3. Identify Misconfigurations
4. Apply Fixes
5. Re-Scan (Closed Loop)

---

## 📊 Final Outcome

* Reduced attack surface
* Improved CIS compliance
* Better internal visibility

---

## 🧠 Key Learnings

* Authenticated scans provide deeper insights
* Misconfigurations are critical risks
* Continuous monitoring is essential

---

## 🏁 Conclusion

VulnVision 360 demonstrates a real-world approach to vulnerability management by combining:

* Vulnerability scanning (OpenVAS)
* Compliance checking (OpenSCAP)
* Remediation validation

---

## ⚠️ Final Note

**"Trust No One. Verify Everything."**
