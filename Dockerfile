FROM ruby:3.2

# 替换 Debian 源为清华源
RUN echo "" > /etc/apt/sources.list && \
    echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian bookworm main contrib non-free non-free-firmware" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian bookworm-updates main contrib non-free non-free-firmware" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian-security bookworm-security main contrib non-free non-free-firmware" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y \
        build-essential \
        nodejs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app    

COPY Gemfile ./


ARG HTTP_PROXY
ARG HTTPS_PROXY
ENV http_proxy=$HTTP_PROXY
ENV https_proxy=$HTTPS_PROXY

RUN gem sources --clear-all
RUN gem sources --add https://mirrors.aliyun.com/rubygems/ --remove https://rubygems.org/
RUN gem sources -l
# RUN bundle config mirror.https://rubygems.org https://mirrors.aliyun.com/rubygems/
RUN gem install bundler:2.3.26
RUN bundle config mirror.https://rubygems.org https://gems.ruby-china.com
RUN bundle install

CMD ["jekyll", "serve", "-H", "0.0.0.0", "-w", "--livereload", "--config", "_config.yml,_config_docker.yml"]