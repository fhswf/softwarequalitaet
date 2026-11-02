FROM mcr.microsoft.com/playwright:v1.40.0-jammy

# Install XFCE, VNC, missing icon themes (fixes broken icons), and a standard browser (fixes taskbar)
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    xfce4 \
    xfce4-goodies \
    tightvncserver \
    novnc \
    websockify \
    adwaita-icon-theme \
    tango-icon-theme \
    firefox \
    && rm -rf /var/lib/apt/lists/*

# Fix the default browser for the XFCE taskbar icon
RUN update-alternatives --set x-www-browser /usr/bin/firefox || true

ENV USER=root
ENV DISPLAY=:99
ENV RESOLUTION=1920x1080

# Clean startup (no Playwright auto-start, just a clean desktop)
RUN echo '#!/bin/bash\n\
rm -rf /tmp/.X99-lock /tmp/.X11-unix/X99\n\
mkdir -p ~/.vnc\n\
echo "password" | vncpasswd -f > ~/.vnc/passwd\n\
chmod 600 ~/.vnc/passwd\n\
vncserver :99 -geometry $RESOLUTION -depth 24\n\
websockify --web /usr/share/novnc/ 6080 localhost:5999 &\n\
tail -f /dev/null' > /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Setup Desktop Shortcuts pointing directly to Uebung5
RUN mkdir -p /root/Desktop
RUN echo '[Desktop Entry]\nVersion=1.0\nType=Application\nName=Playwright Codegen\nExec=bash -c "npx playwright codegen https://demo.playwright.dev/todomvc/"\nIcon=utilities-terminal\nTerminal=false\nPath=/workspace/Uebung5' > /root/Desktop/Codegen.desktop
RUN echo '[Desktop Entry]\nVersion=1.0\nType=Application\nName=Playwright UI\nExec=bash -c "npx playwright test --ui"\nIcon=utilities-terminal\nTerminal=false\nPath=/workspace/Uebung5' > /root/Desktop/Test-UI.desktop
RUN echo '[Desktop Entry]\nVersion=1.0\nType=Application\nName=Terminal\nExec=xfce4-terminal --working-directory=/workspace/Uebung5\nIcon=utilities-terminal\nTerminal=false' > /root/Desktop/Terminal.desktop
RUN chmod +x /root/Desktop/*.desktop

# Ensure we work inside the correct exercise folder
WORKDIR /workspace/Uebung5
ENTRYPOINT ["/entrypoint.sh"]