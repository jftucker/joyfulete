module.exports = {
  apps: [
    {
      name: "joyfulete",
      script: "npm",
      args: "start",
      env_production: {
        NODE_ENV: "dev",
      },
    },
  ],

  deploy: {
    production: {},
    staging: {
      user: "your-user",
      host: "your-server",
      ref: "origin/master",
      repo: "git@github.com:gituser/yourrepo.git",
      path: "/var/www/yourprojectpath",
      key: "/absolute/path/to/key",
      ssh_options: ["ForwardAgent=yes"],
      "post-deploy":
        "npm install && pm2 reload ecosystem.config.js --env production",
    },
    dev: {},
  },
};
