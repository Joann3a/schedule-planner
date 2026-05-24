#!/usr/bin/env python3
"""Serve the schedule-planner on LAN for iPhone access."""
import http.server
import socket
import sys
import os

PORT = 8080

# Change to the directory containing this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Print LAN IP
def get_lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "无法获取IP"

lan_ip = get_lan_ip()
print(f"""
========================================
  日程规划助手 - 移动端服务器
========================================
  本地访问: http://localhost:{PORT}
  iPhone访问: http://{lan_ip}:{PORT}

  请在iPhone上打开浏览器，输入上面的地址
  然后将网页添加到主屏幕 (分享 → 添加到主屏幕)
========================================

按 Ctrl+C 停止服务器
""")

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

http.server.HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
