# #!/bin/bash
# set -e

# # Colors
# RED='\033[0;31m'
# GREEN='\033[0;32m'
# YELLOW='\033[1;33m'
# NC='\033[0m'

# echo -e "${YELLOW}Configuring Docker network for China region (1panel/Proxy Mirrors)...${NC}"

# # Configure Mirrors
# echo -e "\n${YELLOW}Configuring Registry Mirrors...${NC}"

# # Prioritizing Xuanyuan, 1panel and Cloudflare-based reverse proxies. 
# # Removed University mirrors.
# cat <<EOF | sudo tee /etc/docker/daemon.json
# {
#   "registry-mirrors": [
#     "https://docker.xuanyuan.me",
#     "https://docker.1panel.live",
#     "https://hub.rat.dev",
#     "https://docker.anyhub.us.kg",
#     "https://docker.chenby.cn",
#     "https://docker.m.daocloud.io"
#   ],
#   "log-driver": "json-file",
#   "log-opts": {
#     "max-size": "100m",
#     "max-file": "3"
#   }
# }
# EOF

# # Restart Docker
# echo -e "\n${YELLOW}Restarting Docker...${NC}"
# sudo systemctl daemon-reload
# sudo systemctl restart docker

# echo -e "\n${GREEN}Docker configuration updated!${NC}"
# echo "Current Info:"
# docker info | grep -E "Registry Mirrors" -A 10 || true
