# 01 · USB HID — Browser Redirect

**A small Flipper Zero keyboard-emulation demonstration for macOS.**

## Overview

The included [payload](./Payload_BadKB_LinkedIn_Redirect.txt.txt) demonstrates how a USB device emulating a keyboard can perform ordinary keyboard actions on a computer. In this example, the sequence opens **Safari** using Spotlight and navigates to a **legitimate LinkedIn profile**.

This is an awareness demonstration about trusting newly connected USB devices. It does **not** collect credentials, install software, or demonstrate a real phishing compromise.

## Environment

- Device: Flipper Zero with keyboard-emulation support
- Computer: macOS
- Keyboard layout: US English / QWERTY
- Destination: public LinkedIn profile

## What I learned

- How HID keyboard automation interacts with desktop shortcuts
- Why keyboard layout and application startup timing matter
- Why unfamiliar USB accessories deserve the same scrutiny as other untrusted inputs

## Responsible-use note

Run only on a machine you own or have explicit authorization to test. The demonstration uses a benign destination; it should not be repurposed to direct unsuspecting users to harmful websites.

[← Back to lab overview](../README.md)
