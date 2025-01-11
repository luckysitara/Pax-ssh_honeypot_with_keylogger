SnoopPot
---

### **Slide 1: Title Slide**
**Title:** Combined SSH Honeypot and Keylogger Tool  
**Subtitle:** Enhancing Cybersecurity through Advanced Monitoring  
**Your Name:** [Pax]  
**Date:** [DD-MM-YYYY]  

---

### **Slide 2: Introduction**
- **Overview**:  
  A tool combining a honeypot and keylogger that monitors malicious activity.  
- **Importance**:  
  Protects systems by studying attacker behavior and logging data for analysis.  
- **Objectives**:  
  - Simulate an SSH server to attract attackers.  
  - Log key attacker interactions for cybersecurity insights.  

---

### **Slide 3: Project Overview**
- **Components**:  
  - SSH Honeypot: Simulates an SSH server.  
  - Keylogger: Logs keystrokes for analysis.  
  - Logging System: Centralized collection of attacker interactions.  
  - Data Analysis: Extracts insights from attacker behavior.  
- **High-Level Architecture**:  

---

### **Slide 4: Key Components**
1. **SSH Honeypot**:  
   - Captures login attempts, passwords, and issued commands.  
2. **Keylogger**:  
   - Captures user keystrokes on the system.  
3. **Logging**:  
   - Records all interactions with the honeypot and keylogger.  
4. **Data Analysis**:  
   - Provides insights into attacker behavior and generates reports.  

---

### **Slide 5: Tools and Technologies**
- **Programming Language**: Python  
- **Libraries Used**:  
  - `paramiko`: SSH server simulation.  
  - `pynput`: Keylogging.  
  - `logging`: Comprehensive logging.  
---

### **Slide 6: Setup Instructions**
1. **Install Python**: Ensure Python 3.x is installed.  
2. **Clone Repository**:  
   ```bash
   git clone https://github.com/Pax-ssh_honeypot_with_keylogger.git  
   cd Pax-ssh_honeypot_with_keylogger  
   ```  
3. **Install Dependencies**:  
   ```bash
   pip install paramiko pynput  
   ```  
4. **Generate RSA Key**:  
   ```bash
   python generate_rsa_key.py  
   ```  

---

### **Slide 7: Running the Tool**
- **Start the Tool**:  
   ```bash
   python honey.py  
   ```  
   - Honeypot listens on port 2222.  
   - Keylogger begins capturing system keystrokes.  
- **Monitor Logs**: Output logs show all attacker interactions.  

---

### **Slide 8: Simulating an Attacker**
- **Connecting to the Honeypot**:  
   ```bash
   ssh attacker@localhost -p 2222  
   ```  
- **Example Commands Used by Attackers**:  
  - `ls`, `cat /etc/passwd`, `sudo su`.  
- **Result**: Logs attacker actions and records keystrokes for forensic analysis.  

---

### **Slide 9: Monitoring Logs and Analysis**
- **Log File**:  
  - Details SSH login attempts, commands, and keystrokes.  
  - Example:  
    ```log
    [2025-01-10 12:00:00] SSH Login Attempt: user=attacker, password=1234  
    [2025-01-10 12:01:00] Command Executed: ls  
    [2025-01-10 12:02:00] Keystrokes Captured: sudo password  
    ```  
- **Analysis Tools**: Use ELK or Splunk for better insights.  

---

### **Slide 10: Ethical and Legal Considerations**
- **Consent**: Obtain permission before deploying.  
- **Legal Compliance**: Adhere to local laws regarding monitoring.  
- **Privacy**: Limit data collection to avoid misuse.  
- **Transparency**: Inform users in shared environments about monitoring.  

---

### **Slide 11: Use Cases**
1. **Cybersecurity Training**:  
   - Simulates real-world attack scenarios for professionals.  
2. **Threat Intelligence**:  
   - Understand attacker techniques and behavior.  
3. **Incident Response**:  
   - Analyze attack data for remediation.  
4. **Research**:  
   - Study evolving cyber threats.  

---

### **Slide 12: Features**
- **SSH Honeypot**: Simulates an SSH server for attackers.  
- **Keylogger**: Logs all keystrokes for analysis.  
- **Centralized Logging**: Unified logs of attacker activity.  
- **Customizable**: Expand to other services (FTP, HTTP).  

---

### **Slide 13: Future Enhancements**
1. **Advanced Logging**:  
   - Add geolocation or attacker device details.  
2. **Machine Learning**:  
   - Detect unusual patterns in data.  
3. **Improved Analysis Tools**:  
   - Deeper insights using ELK or Splunk.  
4. **Enhanced Services**:  
   - Simulate other protocols like FTP or HTTP.  

---

### **Slide 14: Challenges**
- **Detection by Attackers**: Sophisticated attackers may recognize the honeypot.  
- **Ethical Dilemmas**: Balancing monitoring with privacy.  
- **Scalability**: Adapting the tool for large-scale deployments.  

---

### **Slide 15: Conclusion**
- **Summary**:  
  - The combined tool enhances cybersecurity through real-time attacker monitoring.  
  - Ethical and legal considerations are critical for deployment.  
- **Takeaway**:  
  - A proactive approach to understanding and mitigating cyber threats.  
- **Thank You**

  
