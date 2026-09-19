export type ExamDomain =
  | "Prompting & Task Decomposition"
  | "Evaluation, Fact-Checking & Safety"
  | "Output Formats & Feature Selection"
  | "Model Selection & Context Management"
  | "Business Workflow Integration"
  | "Projects & Knowledge Management"
  | "API Mechanics & Tool Use"
  | "Architectural Patterns & Prompt Caching";

export type DifficultyLevel = "Associate" | "Architect-Foundational";

export interface KeyframeVisualSpec {
  initialFramePrompt: string; // Seedream visual prompt for 00:00 (start keyframe)
  endFramePrompt: string;     // Seedream visual prompt for target state (end keyframe)
  cameraMotion: string;       // Interpolation motion directive (e.g., 'dolly-in zoom', 'pan right')
  styleAnchor: string;        // Consistent aesthetic style anchor token
}

export interface VideoScript16s {
  hook: string;             // 00:00 - 00:03 (Pattern interrupt / core question)
  conceptPart1: string;     // 00:03 - 00:08 (Mechanism & principles)
  conceptPart2: string;     // 00:08 - 00:13 (Applied architecture / exam scenario)
  ctaExamTip: string;       // 00:13 - 00:16 (High-yield exam takeaway)
}

export interface ExamTrap {
  myth: string;
  reality: string;
  examClue: string;
}

export interface ClaudeTermEntry {
  id: string;                      // slug, e.g. "artifacts-vs-inline"
  term: string;                    // Official display title
  acronym?: string;                // e.g. "COT", "MCP"
  domain: ExamDomain;              // 1 of 8 curriculum clusters
  tier: DifficultyLevel;           // Exam tier
  shortDefinition: string;         // 1-2 sentence core definition
  officialExamTopic: string;       // Exact mapping to official topic
  examImportance: "Critical" | "High" | "Medium"; // Curriculum weight
  confirmedCurriculumGap: boolean; // True for topics with 0% candidate baseline
  keyExamTrap: ExamTrap;           // Specific trap candidates fail on
  codeOrSyntaxSnippet?: string;    // JSON, XML, or API parameter snippet
  video16sBlueprint: VideoScript16s; // Ready for Remotion / fal.ai pipeline
  keyframeVisualSpec: KeyframeVisualSpec; // Initial & End frame image generation prompts
  relatedTermIds: string[];        // Graph connections
}

export interface ClaudeAssociateDictionaryDataset {
  version: string;
  lastUpdated: string;
  exam: "Anthropic Claude Certified Associate";
  totalTerms: number;
  domains: {
    name: ExamDomain;
    description: string;
    weightPercentage: number;
  }[];
  terms: ClaudeTermEntry[];
}
