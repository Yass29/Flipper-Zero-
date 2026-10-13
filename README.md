# 🔐 Flipper Zero — Security Learning Lab

**Hands-on hardware security experiments, Python tooling, and responsible security research.**

This repository documents my personal experiments with the **Flipper Zero**, from USB keyboard emulation to Sub-GHz signal formats and read-only device-data reporting. The goal is to understand how these technologies work, document limitations, and practice technical investigation in **controlled, authorized environments**.

**Focus:** Flipper Zero · Python · HID/BadUSB · Sub-GHz · BLE · NFC · Technical documentation

> **Safety & scope:** These projects are for education and testing on devices I own or am explicitly authorized to assess. They are not evidence of bypassing modern access-control systems, and I do not recommend transmitting signals to systems without permission.

## 🧪 Lab projects

| Project | Focus | What's in the repository | Status |
| --- | --- | --- | --- |
| **[01 · USB HID: Browser Redirect](./01_BadKB_LinkedIn_Redirect/)** | USB keyboard emulation, macOS | A demonstration payload that opens a public LinkedIn profile, plus documentation | Documented demo |
| **[02 · Sub-GHz: Code Sequence Generator](./02_SubGHz_RollingCode_Bruteforce/)** | Python, RF file formats | An experimental generator for sequential code values and notes on its assumptions | Experimental; not a verified rolling-code exploit |
| **[03 · Multi-Protocol Recon & Reporting](./03_MultiProtocol_Recon/)** | BLE, NFC, Sub-GHz, Python | Sample CSV exports, basic parsers, an HTML report generator, and early dashboard files | Work in progress |

## 🧠 What I'm practicing

- **Understanding interfaces:** how HID devices, radio metadata, and discovery records are represented
- **Scripting:** processing small datasets and generating structured outputs with Python
- **Reporting:** translating observations into readable documentation and simple HTML reports
- **Security thinking:** distinguishing a proof of concept from a validated vulnerability, and documenting authorization and limitations

## 📂 Repository structure

```text
01_BadKB_LinkedIn_Redirect/       # macOS HID demonstration and notes
02_SubGHz_RollingCode_Bruteforce/ # Experimental Python generator and notes
03_MultiProtocol_Recon/           # Sample exports, scripts, HTML report, early dashboard
README.md                         # Lab overview
```

The folder names reflect the original experiment names; the descriptions above clarify what the committed material actually demonstrates.

## ▶️ Exploring the examples

Start with each project's README for background and current limitations. The **Multi-Protocol Recon** example can process included sample CSV data into a basic HTML report using Python's standard library; it is not yet a complete live device scanner.

Some experimental files are placeholders, and the Sub-GHz code has **not been validated here** as a working rolling-code attack or a Flipper-compatible transmission workflow. Treat those materials as learning notes rather than production-ready tools.

## 🛡️ Responsible use

- Work only on equipment you own or have explicit written permission to test.
- Prefer offline analysis, provided examples, and simulated data.
- Avoid collecting identifying information from other people's devices.
- Follow local radio regulations and device limitations.
- Never assume a theoretical sequence proves an exploitable security weakness.

---

### 👋 About me

I'm **Yasmine**, a Computer Science graduate based in Montréal, interested in software development, IT, and cybersecurity. I build small projects to learn by doing and document what I discover.

**[🌐 Portfolio](https://mon-portfolio-mu-taupe.vercel.app/) · [💻 GitHub](https://github.com/Yass29) · [💼 LinkedIn](https://www.linkedin.com/in/yasmine-ben-youssef-14a9b722a/)**
