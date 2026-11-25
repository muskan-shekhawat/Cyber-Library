export type DifficultyLevel = "Beginner" | "Intermediate" | "Advanced";

export interface KeyConcept {
  term: string;
  definition: string;
}

export interface CodeBlock {
  title: string;
  language: string;
  code: string;
  explanation: string;
}

export interface PracticalExercise {
  title: string;
  scenario: string;
  steps: string[];
  expectedOutcome: string;
}

export interface ReferenceLink {
  title: string;
  url: string;
}

export interface Chapter {
  slug: string;
  chapterNumber: number;
  title: string;
  summary: string;
  introduction: string;
  detailedExplanation: string;
  keyConcepts: KeyConcept[];
  commandsOrCode: CodeBlock[];
  toolsUsed: string[];
  commonMistakes: string[];
  bestPractices: string[];
  practicalExercise: PracticalExercise;
  references: ReferenceLink[];
}

export interface Book {
  slug: string;
  title: string;
  subtitle: string;
  category: string;
  rowId: string;
  volumeNumber: string;
  coverImage: string;
  accentColor: string;
  difficulty: DifficultyLevel;
  estimatedHours: number;
  chaptersCount: number;
  shortDescription: string;
  fullDescription: string;
  learningObjectives: string[];
  toolsCovered: string[];
  relatedBookSlugs: string[];
  chapters: Chapter[];
}

export interface BookRowCategory {
  id: string;
  number: string;
  title: string;
  subtitle: string;
  bookSlugs: string[];
}

export interface ToolItem {
  slug: string;
  name: string;
  category: "Networking" | "Kali Linux" | "Linux" | "OSINT" | "Digital Forensics" | "Malware Analysis" | "SOC" | "Python";
  officialWebsite: string;
  officialDocs: string;
  purpose: string;
  installation: {
    linux?: string;
    macos?: string;
    windows?: string;
  };
  basicUsage: string;
  safeExamples: {
    title: string;
    command: string;
    description: string;
    expectedOutput?: string;
  }[];
  relatedBookSlugs: string[];
}
