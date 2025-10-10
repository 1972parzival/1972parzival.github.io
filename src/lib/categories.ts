// Category Configuration
export interface Category {
  slug: string;
  name: string;
  description: string;
  icon: string;
  color: string;
  aliases?: string[]; // Add aliases for alternative URLs
}

export const categories: Category[] = [
  // Primary project categories based on content analysis
  {
    slug: '3d-printing-manufacturing',
    name: '3D Printing & Manufacturing',
    description: 'Design, printing, prototyping, and manufacturing processes',
    icon: '🔧',
    color: 'bg-blue-100 text-blue-800',
    aliases: ['3d-printing', 'manufacturing', 'prototyping']
  },
  {
    slug: 'electronics-arduino',
    name: 'Electronics & Arduino',
    description: 'Microcontroller projects, sensors, and electronic circuits',
    icon: '⚡',
    color: 'bg-yellow-100 text-yellow-800',
    aliases: ['electronics', 'arduino', 'microcontroller', 'sensors']
  },
  {
    slug: 'chemistry-materials',
    name: 'Chemistry & Materials',
    description: 'Chemical processes, material science experiments, and laboratory work',
    icon: '🧪',
    color: 'bg-green-100 text-green-800',
    aliases: ['chemistry', 'materials', 'science', 'lab']
  },
  {
    slug: 'software-programming',
    name: 'Software & Programming',
    description: 'Programming projects, software tools, and AI/ML applications',
    icon: '�',
    color: 'bg-purple-100 text-purple-800',
    aliases: ['software', 'programming', 'coding', 'ai', 'ml']
  },
  {
    slug: 'engineering-mechanical',
    name: 'Engineering & Mechanical',
    description: 'Mechanical design, engineering solutions, and problem-solving projects',
    icon: '⚙️',
    color: 'bg-gray-100 text-gray-800',
    aliases: ['engineering', 'mechanical', 'design']
  },
  {
    slug: 'academic-documentation',
    name: 'Academic & Documentation',
    description: 'Educational content, research, documentation, and academic work',
    icon: '�',
    color: 'bg-indigo-100 text-indigo-800',
    aliases: ['academic', 'documentation', 'research', 'education']
  },
  {
    slug: 'tools-utilities',
    name: 'Tools & Utilities',
    description: 'Tool making, utility projects, and workshop improvements',
    icon: '�',
    color: 'bg-orange-100 text-orange-800',
    aliases: ['tools', 'utilities', 'workshop']
  },
  {
    slug: 'creative-media',
    name: 'Creative & Media',
    description: 'Creative projects, media production, and artistic endeavors',
    icon: '🎨',
    color: 'bg-pink-100 text-pink-800',
    aliases: ['creative', 'media', 'art', 'design']
  },
  {
    slug: 'work-services',
    name: 'Work & Services',
    description: 'Professional work, client services, and business projects',
    icon: '💼',
    color: 'bg-teal-100 text-teal-800',
    aliases: ['work', 'services', 'business', 'professional']
  },
  {
    slug: 'personal',
    name: 'Personal',
    description: 'Personal projects, interests, and individual pursuits',
    icon: '👤',
    color: 'bg-cyan-100 text-cyan-800',
    aliases: ['personal', 'individual']
  },
  {
    slug: 'experimental',
    name: 'Experimental',
    description: 'Experimental work, prototypes, and testing phases',
    icon: '�',
    color: 'bg-red-100 text-red-800',
    aliases: ['experimental', 'prototype', 'testing']
  },
  {
    slug: 'tutorial',
    name: 'Tutorial',
    description: 'Instructional content, how-to guides, and educational materials',
    icon: '�',
    color: 'bg-emerald-100 text-emerald-800',
    aliases: ['tutorial', 'guide', 'howto', 'instruction']
  },
  // Legacy categories for backward compatibility
  {
    slug: 'dotnet',
    name: '.NET',
    description: 'ASP.NET, Blazor, C#, and .NET development',
    icon: '🏗️',
    color: 'bg-purple-100 text-purple-800',
    aliases: ['net', 'csharp', 'C#', 'aspnet', 'blazor']
  },
  {
    slug: 'csharp',
    name: 'C#',
    description: 'C# programming language, syntax, and development',
    icon: '�',
    color: 'bg-purple-100 text-purple-800',
    aliases: ['cs', 'C#']
  },
  {
    slug: 'python',
    name: 'Python',
    description: 'Python programming, data science, AI/ML, and automation',
    icon: '🐍',
    color: 'bg-green-100 text-green-800',
    aliases: ['py', 'django', 'flask', 'pandas', 'numpy']
  },
  {
    slug: 'java',
    name: 'Java',
    description: 'Java development, Spring, Android, and JVM technologies',
    icon: '☕',
    color: 'bg-orange-100 text-orange-800',
    aliases: ['spring', 'J2EE', 'kotlin']
  },
  {
    slug: 'sql',
    name: 'SQL',
    description: 'SQL databases, queries, data management, and database development',
    icon: '🗄️',
    color: 'bg-indigo-100 text-indigo-800',
    aliases: ['mysql', 'postgresql', 'sqlserver', 'sqlite']
  },
  {
    slug: 'javascript',
    name: 'JavaScript',
    description: 'JavaScript development, Node.js, React, Angular, and other web frameworks',
    icon: '�',
    color: 'bg-yellow-100 text-yellow-800',
    aliases: ['js', 'nodejs', 'node', 'vue', 'electron', 'nextjs']
  },
  {
    slug: 'azure',
    name: 'Azure',
    description: 'Microsoft Azure cloud services and development',
    icon: '☁️',
    color: 'bg-blue-100 text-blue-800',
    aliases: ['azureai', 'azureopenai', 'azure-functions', 'azure-devops']
  },
  {
    slug: 'ai',
    name: 'AI',
    description: 'Artificial Intelligence, machine learning, and AI models',
    icon: '🤖',
    color: 'bg-green-100 text-green-800',
    aliases: ['artificial-intelligence', 'machine-learning', 'ml', 'openai', 'chatgpt']
  },

];

// Category Helper Functions
export function getCategoryBySlug(slug: string): Category | undefined {
  return categories.find(category =>
    category.slug === slug ||
    (category.aliases && category.aliases.includes(slug))
  );
}

export function getCategoryByName(name: string): Category | undefined {
  return categories.find(cat => cat.name === name);
}

export function categoryNameToSlug(name: string): string {
  return name.toLowerCase().replace(/\s+/g, '-').replace(/&/g, '');
}

export function categorySlugToName(slug: string): string {
  const category = getCategoryBySlug(slug);
  return category ? category.name : slug;
}

