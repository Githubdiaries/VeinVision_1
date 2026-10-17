sudo systemctl status mediamtx --no-pager
curl -f http://127.0.0.1:8888/cam/index.m3u8 | head
sudo tailscale serve status