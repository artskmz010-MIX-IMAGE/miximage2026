# 🎨 Miximage AI 2026

**AI-powered portrait generation studio with intelligent 7-layer customization**

Create stunning AI-generated portraits with real-time preview and professional-grade output.

![Version](https://img.shields.io/badge/Version-0.1.0--alpha-blue)
![Status](https://img.shields.io/badge/Status-Development-yellow)
![License](https://img.shields.io/badge/License-MIT-green)
![Node](https://img.shields.io/badge/Node-18+-green)

---

## ✨ Key Features

- **📸 AI Photo Analysis** - Automatic gender detection using Gemini AI
- **🎨 7-Layer Style Customization** - Full control over portrait generation:
  - Aspect Ratio (3:4, 2:3, 1:1, 9:16)
  - Outfit & Color Selection (40+ options)
  - Background Customization (Studio, Location, Memorial)
  - **Professional Lighting Options (17 styles)** - Classic, Studio, Natural, Creative
  - Pose & Expression Control
  - Hair Style & Color
  - **Makeup & Retouching (25+ styles)** - Multi-select support

- **✨ AI-Powered Prompt Generation** - Smart prompt building with Lovable API
- **🖼️ Portrait Generation** - High-quality image generation using Gemini 3 Pro
- **🚀 Real-time Preview** - Instant visual feedback
- **💾 Professional Export** - Production-ready assets

---

## 🆕 Recent Updates

### Multi-Select Support (v0.1.0)
- **Lighting**: เลือกได้หลายรูปแบบพร้อมกัน (เช่น Rembrandt + Rim Light)
- **Makeup/Retouch**: ผสมผสานหลายสไตล์ (เช่น Natural Polish + V-Shape + Nude Lips)

### Enhanced Style Library
- **Lighting Categories**: Classic (6), Studio (4), Natural (3), Creative (3)
- **Makeup/Retouch**: Base (4), Contour (3), Eyes (5), Lips (5), Looks (6) สำหรับผู้หญิง
- **Male Grooming**: Skin (3), Contour (3), Eyes (2), Grooming (3)

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | React 18 + TypeScript + Vite |
| **Styling** | Tailwind CSS + shadcn-ui |
| **State** | React Query + React Hooks |
| **Backend** | Lovable Cloud (Supabase) |
| **AI API** | Lovable AI Gateway (Gemini Models) |
| **Deployment** | Lovable Publish |

---

## ⚡ 15-Minute Bring-Up Checklist

ต้องการให้โปรเจกต์รันขึ้นเร็ว ดูขั้นตอนแบบเร่งด่วนที่ `CHECKLIST_15MIN.md`

---

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ ([Install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating))
- npm or bun
- Lovable API key (for AI features)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/miximage/Miximage-ai-2026.git
cd Miximage-ai-2026

# 2. Install dependencies
npm install
# or
bun install

# 3. Set up environment variables (see below)
cp .env.example .env.local

# 4. Start development server
npm run dev
# App will be available at http://localhost:5173
```

### Development Commands

```bash
# Start dev server with hot reload
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint
```

---

## ⚙️ Environment Variables

Create a `.env.local` file in the root directory with the following variables:

```env
# Lovable Cloud Configuration (auto-configured in Lovable)
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_PUBLISHABLE_KEY=your-anon-key

# Optional
VITE_APP_NAME=MIX IMAGE AI 2026
VITE_ENV=development
```

For local development, copy `.env.example` and fill in your credentials:

```bash
cp .env.example .env.local
```

---

## 📁 Project Structure

```
src/
├── components/          # React components
│   └── studio/         # Main Studio panel components
│       ├── StudioPanel.tsx      # Main control panel
│       ├── StyleChips.tsx       # Single-select chips
│       ├── MultiStyleChips.tsx  # Multi-select chips
│       ├── ImageUploader.tsx    # Image upload handling
│       └── WorkspaceCanvas.tsx  # Preview canvas
├── lib/                # Utilities and services
│   ├── aiService.ts    # AI API integrations
│   ├── styleConstants.ts # 7-layer style options (329 lines)
│   └── promptBuilder.ts # AI prompt generation
├── integrations/       # Third-party integrations
│   └── supabase/       # Lovable Cloud client
├── pages/              # Page components
└── App.tsx             # Root component

supabase/
└── functions/          # Edge Functions
    ├── analyze-photo/  # Gender detection
    ├── draft-prompt/   # AI prompt generation
    └── generate-portrait/ # Image generation
```

---

## 🎯 How to Use

### 1. Upload Photo
- Click "Upload Image" and select your photo
- The app automatically detects gender and suggests matching styles

### 2. Customize Styles
Select from 7 customization layers:
- Choose aspect ratio
- Pick outfit and colors
- Select background and lighting (multi-select)
- Configure pose, hair, and makeup (multi-select)

### 3. Generate
- Click "Analyze & Draft" to create AI prompt
- Click "Generate Final Image" to create portrait

### 4. Export
- Download high-resolution portrait
- Perfect for professional use

---

## 🔌 API Integration

### Edge Functions

The app uses Lovable Cloud Edge Functions for AI operations:

1. **analyze-photo** - Detects gender from uploaded image
2. **draft-prompt** - Generates detailed AI prompt based on selections
3. **generate-portrait** - Creates final portrait using Gemini models

### Lovable AI Gateway

Uses Lovable's unified AI API to access:
- Google Gemini 2.5 Flash (analysis)
- Google Gemini 3 Pro (image generation)

---

## 📦 Build & Deployment

### Build for Production

```bash
npm run build
# Output: dist/ directory
```

### Deploy with Lovable (Recommended)

Click the "Publish" button in Lovable to deploy instantly.

### Custom Domain

Connect your custom domain in Lovable Project Settings → Domains.

---

## 🎨 Style Reference Sources

### Lighting Techniques
- [Classic Portrait Lighting Patterns](https://gmhsart.weebly.com/classic-lighting.html)
- [Studio Photography Lighting Techniques](https://www.colborlight.com/blogs/articles/studio-photography-lighting-techniques)

### Makeup & Retouching
- [Best Makeup for Photoshoot](https://renataclarkeportraits.com/best-makeup-for-photoshoot/)
- [Natural vs Glamour Photoshoot](https://www.fontainephotography.ca/latest-news-events-and-tips/natural-makeup-glamour-photoshoot)
- [Camera Ready Makeup Guide](https://alimondphotography.com/camera-ready-makeup-nailing-the-natural-vs-glamorous-headshot-look/)

---

## 🤝 Contributing

We welcome contributions! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow TypeScript best practices
- Use eslint for code quality
- Test changes locally before pushing
- Update README if adding features

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🐛 Known Issues & Roadmap

### Current Limitations
- Batch processing not yet supported
- Limited error recovery
- No analytics tracking

### Coming Soon 🚧
- [ ] Batch image processing
- [ ] Advanced error handling & retries
- [ ] Analytics and usage tracking
- [ ] API documentation
- [ ] Unit tests for AI services
- [ ] Production deployment pipeline

---

## 💬 Support & Feedback

- 📧 Email: support@miximage.ai
- 💬 Issues: [GitHub Issues](https://github.com/miximage/Miximage-ai-2026/issues)

---

## 🙏 Credits

Built with ❤️ by [Natthanan Miximage](https://github.com/miximage)

- AI Models: Google Gemini
- UI Components: shadcn-ui + Radix UI
- Backend: Lovable Cloud
- API: Lovable AI Gateway

---

*Last updated: 2026-01-04*
