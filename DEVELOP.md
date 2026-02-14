# 🚀 GitHub Stats

Generate dynamic, customizable SVG cards displaying GitHub user statistics for your README files!

Inspired by [github-readme-stats](https://github.com/anuraghazra/github-readme-stats) by Anurag Hazra.

## ✨ Features

- 📊 Dynamic GitHub stats generation
- 🎨 70+ built-in themes
- 🔧 Highly customizable
- ⚡ Fast API with caching
- 🌐 Easy to deploy
- 💯 TypeScript support

## 📦 Installation

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn
- GitHub Personal Access Token ([Create one here](https://github.com/settings/tokens))

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/github-stats.git
cd github-stats
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file:
```bash
cp .env.example .env
```

4. Add your GitHub token to `.env`:
```
GITHUB_TOKEN=your_github_personal_access_token
PORT=3000
```

5. Build and run:
```bash
npm run build
npm start
```

Or for development:
```bash
npm run dev
```

## 🚀 Usage

### Basic Usage

Add this to your GitHub README:

```markdown
![GitHub Stats](http://localhost:3000/stats?username=YOUR_USERNAME)
```

### With Theme

```markdown
![GitHub Stats](http://localhost:3000/stats?username=YOUR_USERNAME&theme=dark)
```

## 🎨 Available Themes

Choose from over 70 themes:

| Theme | Preview |
|-------|---------|
| `default` | Classic light theme |
| `dark` | Dark theme |
| `radical` | Pink and cyan |
| `merko` | Green terminal style |
| `gruvbox` | Retro groove |
| `tokyonight` | Tokyo night inspired |
| `onedark` | Atom one dark |
| `cobalt` | Deep blue |
| `synthwave` | 80s vibes |
| `highcontrast` | High contrast |
| `dracula` | Dracula theme |
| `prussian` | Prussian blue |
| `monokai` | Monokai |
| `vue` | Vue.js theme |
| `vue-dark` | Vue.js dark |
| `shades-of-purple` | Purple shades |
| `nightowl` | Night owl |
| `buefy-dark` | Buefy dark |
| `blue-green` | Blue and green |
| `algolia` | Algolia theme |
| `great-gatsby` | Great Gatsby |
| `darcula` | JetBrains Darcula |
| `bear` | Bear theme |
| `solarized-dark` | Solarized dark |
| `solarized-light` | Solarized light |
| `chartreuse-dark` | Chartreuse dark |
| `nord` | Nord theme |
| `gotham` | Gotham theme |
| `material-palenight` | Material palenight |
| `graywhite` | Gray and white |
| `vision-friendly-dark` | Vision friendly |
| `ayu-mirage` | Ayu mirage |
| `midnight-purple` | Midnight purple |
| `calm` | Calm theme |
| `flag-india` | Indian flag colors |
| `omni` | Omni theme |
| `react` | React theme |
| `jolly` | Jolly theme |
| `maroongold` | Maroon and gold |
| `yeblu` | Yellow and blue |
| `blueberry` | Blueberry theme |
| `slateorange` | Slate orange |
| `kacho_ga` | Japanese style |
| `outrun` | Outrun style |
| `ocean_dark` | Ocean dark |
| `city_lights` | City lights |
| `github_dark` | GitHub dark |
| `discord_old_blurple` | Discord old blue |
| `aura_dark` | Aura dark |
| `panda` | Panda theme |
| `noctis_minimus` | Noctis minimus |
| `cobalt2` | Cobalt 2 |
| `swift` | Swift theme |
| `aura` | Aura theme |
| `apprentice` | Apprentice theme |
| `moltack` | Moltack theme |
| `codeSTACKr` | CodeSTACKr theme |
| `rose_pine` | Rosé Pine |

## ⚙️ Customization Options

| Parameter | Description | Default |
|-----------|-------------|---------|
| `username` | GitHub username (required) | - |
| `theme` | Theme name | `default` |
| `hide_title` | Hide the card title | `false` |
| `hide_border` | Hide the card border | `false` |
| `hide_rank` | Hide the rank circle | `false` |
| `show_icons` | Show stat icons | `true` |
| `custom_title` | Custom card title | `{name}'s GitHub Stats` |

### Examples

#### Hide Title
```markdown
![GitHub Stats](http://localhost:3000/stats?username=YOUR_USERNAME&hide_title=true)
```

#### Hide Border
```markdown
![GitHub Stats](http://localhost:3000/stats?username=YOUR_USERNAME&hide_border=true)
```

#### Hide Rank
```markdown
![GitHub Stats](http://localhost:3000/stats?username=YOUR_USERNAME&hide_rank=true)
```

#### Custom Title
```markdown
![GitHub Stats](http://localhost:3000/stats?username=YOUR_USERNAME&custom_title=My%20Awesome%20Stats)
```

#### Combined Options
```markdown
![GitHub Stats](http://localhost:3000/stats?username=YOUR_USERNAME&theme=tokyonight&hide_border=true&show_icons=true)
```

## 📊 Stats Displayed

The card shows the following statistics:

- ⭐ **Total Stars** - Stars earned across all repositories
- 📝 **Total Commits** - Total commits made (all-time)
- 🔀 **Total PRs** - Total pull requests created
- 🐛 **Total Issues** - Total issues created
- 🤝 **Contributed to** - Number of repositories contributed to
- 🏆 **Rank** - Calculated rank based on your contributions (S+, S, A+, A, B+, B, C)

## 🏗️ Project Structure

```
github-stats/
├── src/
│   ├── index.ts           # Main Express server
│   ├── github-client.ts   # GitHub API client
│   ├── card-renderer.ts   # SVG card generator
│   ├── themes.ts          # Theme definitions
│   └── types.ts           # TypeScript types
├── dist/                  # Compiled JavaScript
├── package.json
├── tsconfig.json
├── .env.example
├── .gitignore
└── README.md
```

## 🔧 Development

### Build
```bash
npm run build
```

### Run in Development Mode
```bash
npm run dev
```

### Run in Production
```bash
npm start
```

## 🚢 Deployment

### Deploy to Vercel

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel
```

3. Add environment variable `GITHUB_TOKEN` in Vercel dashboard

### Deploy to Heroku

1. Create a Heroku app:
```bash
heroku create your-app-name
```

2. Set environment variable:
```bash
heroku config:set GITHUB_TOKEN=your_token
```

3. Deploy:
```bash
git push heroku main
```

### Deploy to Railway

1. Connect your GitHub repository to Railway
2. Add environment variable `GITHUB_TOKEN`
3. Railway will automatically deploy

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by [github-readme-stats](https://github.com/anuraghazra/github-readme-stats) by Anurag Hazra
- Themes adapted from various popular editor themes
- Icons from [Octicons](https://primer.style/octicons/)

## 📧 Contact

For questions or support, please open an issue on GitHub.

## 🌟 Star History

If you like this project, please give it a star! ⭐

---

Made with ❤️ and TypeScript
