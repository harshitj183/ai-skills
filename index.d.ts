export interface TrustPolicies {
  require_hash: boolean;
  audit_on_fetch: string;
  whitelist_domains: string[];
}

export interface SkillSource {
  name: string;
  url: string;
  description?: string;
  verified_hash?: string;
}

export interface SkillEntry {
  name: string;
  url: string;
}

export interface SkillBank {
  version: string;
  name: string;
  trust_policies: TrustPolicies;
  power_sources: SkillSource[];
  registries_optimized: {
    [category: string]: SkillEntry[];
  };
}

export const skillBank: SkillBank;
export const version: string;
export function getSkills(): { [category: string]: SkillEntry[] };
export function getTrustPolicies(): TrustPolicies;
