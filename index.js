const skillBank = require('./registry/skill_bank.json');

module.exports = {
  skillBank,
  version: skillBank.version,
  getSkills: () => skillBank.registries_optimized,
  getTrustPolicies: () => skillBank.trust_policies
};
