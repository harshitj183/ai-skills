#!/usr/bin/env node

const fs = require('fs-extra');
const path = require('path');
const { program } = require('commander');
const inquirer = require('inquirer');

// ANSI Terminal Colors
const colors = {
    reset: "\x1b[0m",
    bright: "\x1b[1m",
    green: "\x1b[32m",
    blue: "\x1b[34m",
    cyan: "\x1b[36m",
    yellow: "\x1b[33m",
    red: "\x1b[31m"
};

const targetDir = process.cwd();
const sourceDir = path.join(__dirname, '..');
const targetDirBase = path.join(targetDir, 'smart-instructions');

program
  .name('ai-skills')
  .description('The Ultimate AI Skill Library CLI')
  .version('2.2.6');

program
  .command('init')
  .description('Installs the Smart AI Skills Library')
  .option('-i, --interactive', 'Run interactively to select specific roles/skills')
  .option('-r, --roles <roles>', 'Comma-separated list of roles to install')
  .option('-s, --skills <skills>', 'Comma-separated list of skills to install')
  .action(async (options) => {
    console.log(`${colors.bright}${colors.cyan}Initializing Smart AI Skills Library...${colors.reset}\n`);

    const availableRoles = fs.existsSync(path.join(sourceDir, 'roles')) ? fs.readdirSync(path.join(sourceDir, 'roles')) : [];
    const availableSkills = fs.existsSync(path.join(sourceDir, 'skills')) ? fs.readdirSync(path.join(sourceDir, 'skills')) : [];

    let selectedRoles = availableRoles;
    let selectedSkills = availableSkills;

    if (options.interactive) {
      const { installType } = await inquirer.prompt([
        {
          type: 'list',
          name: 'installType',
          message: 'How would you like to install the skills?',
          choices: [
            'Install Everything (All 8 Roles, 17 Mega-Skills)',
            'Custom Pick (Select specific roles and skills)'
          ]
        }
      ]);

      if (installType.startsWith('Custom')) {
        const answers = await inquirer.prompt([
          {
            type: 'checkbox',
            name: 'roles',
            message: 'Select the Master Roles you need:',
            choices: availableRoles.filter(f => f.endsWith('.md'))
          },
          {
            type: 'checkbox',
            name: 'skills',
            message: 'Select the Mega-Skills you need:',
            choices: availableSkills.filter(f => f.endsWith('.md'))
          }
        ]);
        selectedRoles = answers.roles;
        selectedSkills = answers.skills;
      }
    } else {
        if (options.roles) {
            const rList = options.roles.split(',').map(r => r.trim());
            selectedRoles = availableRoles.filter(r => rList.includes(r) || rList.includes(r.replace('.md', '')));
        }
        if (options.skills) {
            const sList = options.skills.split(',').map(s => s.trim());
            selectedSkills = availableSkills.filter(s => sList.includes(s) || sList.includes(s.replace('.md', '')));
        }
    }

    if (!fs.existsSync(targetDirBase)) {
        fs.mkdirSync(targetDirBase, { recursive: true });
    }

    console.log(`\n${colors.blue}[+] Securing source control (.gitignore)...${colors.reset}`);
    const ignoreRules = "\n\n# Smart AI Skills Library (Context Only)\nsmart-instructions/\n";
    const gitignorePath = path.join(targetDir, '.gitignore');
    if (fs.existsSync(gitignorePath)) {
        const currentIgnore = fs.readFileSync(gitignorePath, 'utf8');
        if (!currentIgnore.includes('# Smart AI Skills Library')) {
            fs.appendFileSync(gitignorePath, ignoreRules);
        }
    } else {
        fs.writeFileSync(gitignorePath, ignoreRules.trim() + "\n");
    }

    console.log(`${colors.blue}[+] Copying SKILL.md Master Rulebook...${colors.reset}`);
    const targetSkillMd = path.join(targetDirBase, 'SKILL.md');
    if (fs.existsSync(path.join(sourceDir, 'SKILL.md'))) {
        fs.copyFileSync(path.join(sourceDir, 'SKILL.md'), targetSkillMd);
    }
    
    if (selectedRoles.length > 0) {
        console.log(`${colors.blue}[+] Extracting ${selectedRoles.length} Master Roles...${colors.reset}`);
        fs.ensureDirSync(path.join(targetDirBase, 'roles'));
        selectedRoles.forEach(role => {
            fs.copyFileSync(path.join(sourceDir, 'roles', role), path.join(targetDirBase, 'roles', role));
        });
    }

    if (selectedSkills.length > 0) {
        console.log(`${colors.blue}[+] Extracting ${selectedSkills.length} Mega-Skills...${colors.reset}`);
        fs.ensureDirSync(path.join(targetDirBase, 'skills'));
        selectedSkills.forEach(skill => {
            fs.copyFileSync(path.join(sourceDir, 'skills', skill), path.join(targetDirBase, 'skills', skill));
        });
    }

    // Add History tracking for consumer context (Fresh Templates)
    console.log(`${colors.blue}[+] Initializing History tracking logs (Fresh Templates)...${colors.reset}`);
    const targetHistoryDir = path.join(targetDirBase, 'history');
    fs.ensureDirSync(targetHistoryDir);

    const historyTemplates = {
        'history.md': `# 📖 Project History & Context\n\nWelcome to your project's AI history hub. This system is designed to provide context for AI agents working on this project.\n\n### 📂 Modules\n| Module | Description | Link |\n| :--- | :--- | :--- |\n| **[AI Activity Log](ai_activity_log.md)** | Record of AI agent contributions. | [View Log](ai_activity_log.md) |\n| **[Project Timeline](project_timeline.md)** | Roadmap and milestones. | [View Timeline](project_timeline.md) |\n| **[Version History](version_history.md)** | Detailed release logs. | [View Versions](version_history.md) |\n\n---\n*Maintained by: AI Skills History System*`,
        'ai_activity_log.md': `# 🤖 AI Activity Log\n\nThis log tracks specific contributions and tasks performed by AI agents in this project.\n\n---\n\n## 🏃 Active Session (Initial Setup)\n- **Task**: Initialized Smart AI Skills Library (v${program.version()}).\n- **Objective**: Established base AI context and roles library.\n\n---\n*Last updated by: AI Assistant (init)*`,
        'project_timeline.md': `# 📅 Project Timeline\n\nMajor milestones and timeline of this project.\n\n---\n\n### ${new Date().toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}\n- **Initialized**: AI Skills Library integrated into the project.\n\n---\n*Last updated by: AI Assistant (init)*`,
        'version_history.md': `# 📦 Version History\n\nVersion tracking for this specific project.\n\n---\n- **v0.1.0** (${new Date().toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}): Initial setup with Smart AI Skills Library.\n\n---\n*Last updated by: AI Assistant (init)*`,
        'milestones.md': `# 🏆 Project Milestones\n\nTracking the breakthrough moments of this project.\n\n---\n- **Initialization**: Integrated AI Skills Library (v${program.version()}).\n\n---\n*Last updated by: AI Assistant (init)*`
    };

    Object.entries(historyTemplates).forEach(([filename, content]) => {
        fs.writeFileSync(path.join(targetHistoryDir, filename), content);
    });

    console.log(`\n${colors.bright}${colors.green}[Success] The 'smart-instructions' folder has been added to your project!${colors.reset}`);
    console.log(`${colors.yellow}Tip: Let your AI Agent pick skills natively, or run 'npx ai-skills configure' to setup your IDE!${colors.reset}\n`);
  });

program
  .command('configure')
  .description('Auto-configures your IDE to use the skills')
  .action(async () => {
    console.log(`${colors.bright}${colors.cyan}IDE Auto-Configuration${colors.reset}\n`);
    
    const targetSkillMd = path.join(targetDir, 'smart-instructions', 'SKILL.md');
    if (!fs.existsSync(targetSkillMd)) {
        console.error(`${colors.red}[Error] 'smart-instructions/SKILL.md' not found. Please run 'npx ai-skills init' first.${colors.reset}`);
        return;
    }

    const { ideSelection } = await inquirer.prompt([
      {
        type: 'list',
        name: 'ideSelection',
        message: 'Which AI IDE or tool are you using?',
        choices: [
          'Cursor (.cursorrules)',
          'Windsurf (.windsurfrules)',
          'Claude Code (CLAUDE.md)',
          'GitHub Copilot (.github/copilot-instructions.md)',
          'Cline (.clinerules)',
          'Cancel'
        ]
      }
    ]);

    let destPath = '';
    if (ideSelection.startsWith('Cursor')) destPath = '.cursorrules';
    else if (ideSelection.startsWith('Windsurf')) destPath = '.windsurfrules';
    else if (ideSelection.startsWith('Claude')) destPath = 'CLAUDE.md';
    else if (ideSelection.startsWith('GitHub')) destPath = '.github/copilot-instructions.md';
    else if (ideSelection.startsWith('Cline')) destPath = '.clinerules';
    else {
        console.log(`${colors.yellow}Configuration cancelled.${colors.reset}`);
        return;
    }

    const fullDestPath = path.join(targetDir, destPath);
    if (destPath.includes('/')) {
        fs.ensureDirSync(path.dirname(fullDestPath));
    }

    const ruleContent = fs.readFileSync(targetSkillMd, 'utf8');

    if (fs.existsSync(fullDestPath)) {
        const { overwrite } = await inquirer.prompt([
            {
                type: 'confirm',
                name: 'overwrite',
                message: `${destPath} already exists. Do you want to overwrite it?`,
                default: false
            }
        ]);
        if (!overwrite) {
            console.log(`${colors.yellow}Configuration skipped.${colors.reset}`);
            return;
        }
    }

    fs.writeFileSync(fullDestPath, ruleContent);
    console.log(`\n${colors.bright}${colors.green}[Success] ${destPath} has been successfully configured!${colors.reset}\n`);
  });

program
  .command('create <skill_name>')
  .description('Scaffolds a new custom Mega-Skill')
  .action(async (skillName) => {
    console.log(`${colors.bright}${colors.cyan}Custom Skill Scaffolding${colors.reset}\n`);
    
    const { audience, format } = await inquirer.prompt([
      {
        type: 'input',
        name: 'audience',
        message: 'Who is this skill for? (e.g., Frontend React Devs, Backend Node Devs):',
      },
      {
         type: 'confirm',
         name: 'format',
         message: 'Include strict JSON formatting rules?',
         default: true
      }
    ]);

    const customDir = path.join(targetDir, 'smart-instructions', 'custom');
    fs.ensureDirSync(customDir);

    const destFile = path.join(customDir, `${skillName.replace('.md', '')}.md`);

    const template = `# ${skillName} Mega-Skill\n\n## Objective\nProvide expert-level instructions for ${audience}.\n\n## Rules\n- Always prioritize clarity and performance.\n- Write modern, maintainable code.\n${format ? '- ALWAYS output responses in strict JSON format when requested.\n' : ''}\n## Architecture Guidelines\n1. Keep functions small and focused.\n2. Ensure rigorous error handling.\n`;

    fs.writeFileSync(destFile, template);
    console.log(`\n${colors.bright}${colors.green}[Success] Scaffolded new custom skill at ${destFile}!${colors.reset}\n`);
  });

program
  .command('update')
  .description('Updates the official skills without overwriting custom ones in /custom/')
  .action(async () => {
    console.log(`${colors.bright}${colors.cyan}Updating Official Skills${colors.reset}\n`);
    const { proceed } = await inquirer.prompt([
      {
        type: 'confirm',
        name: 'proceed',
        message: 'This will safely copy the latest official skills into smart-instructions/ overriding existing ones. Custom folders will be preserved. Proceed?',
        default: true
      }
    ]);

    if (!proceed) {
        console.log(`${colors.yellow}Update cancelled.${colors.reset}`);
        return;
    }

    try {
        fs.ensureDirSync(path.join(targetDir, 'smart-instructions', 'roles'));
        fs.ensureDirSync(path.join(targetDir, 'smart-instructions', 'skills'));
        
        const rDir = path.join(sourceDir, 'roles');
        if (fs.existsSync(rDir)) fs.copySync(rDir, path.join(targetDir, 'smart-instructions', 'roles'));
        
        const sDir = path.join(sourceDir, 'skills');
        if (fs.existsSync(sDir)) fs.copySync(sDir, path.join(targetDir, 'smart-instructions', 'skills'));

        const hDir = path.join(sourceDir, 'history');
        const targetHistoryDir = path.join(targetDir, 'smart-instructions', 'history');
        if (fs.existsSync(hDir)) {
            // Only update the guide, preserving consumer logs
            const guide = 'history.md';
            fs.ensureDirSync(targetHistoryDir);
            if (fs.existsSync(path.join(hDir, guide))) fs.copyFileSync(path.join(hDir, guide), path.join(targetHistoryDir, guide));
        }

        const targetSkillMd = path.join(targetDir, 'smart-instructions', 'SKILL.md');
        if (fs.existsSync(path.join(sourceDir, 'SKILL.md'))) {
            fs.copyFileSync(path.join(sourceDir, 'SKILL.md'), targetSkillMd);
        }

        console.log(`\n${colors.bright}${colors.green}[Success] Official library updated!${colors.reset}\n`);
    } catch (e) {
        console.error(`${colors.red}[Error] Update failed: ${e.message}${colors.reset}`);
    }
  });

// Handle no arguments gracefully
if (process.argv.length === 2) {
    process.argv.push('--help');
}

program.parse(process.argv);
