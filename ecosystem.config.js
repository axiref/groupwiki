module.exports = {
  apps : [{
    name: 'groupwiki',
    script: 'python bot.py',
    instances: 1,
    autorestart: true,
  }]
};
