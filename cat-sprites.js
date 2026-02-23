// ============================================================
// CAT SPRITE ANIMATION SYSTEM
// Palette-indexed template system for 8 breeds × 12 frames
// ============================================================

// Palette index legend:
// '.' = transparent   '1' = main body      '2' = dark accent/stripe
// '3' = light belly   '4' = eye white/iris bg  '5' = iris color
// '6' = pupil         '7' = nose           '8' = inner ear (pink)
// '9' = patch1        'A' = patch2         'B' = shadow/shading

// ============================================================
// FRAME TEMPLATES (16x16 grids as string arrays)
// Based on exact SVG rect analysis of original sprites
// ============================================================

const FRAME_TEMPLATES = {
  // --- IDLE: standing still, tail up ---
  idle_0: [
    '................',
    '...11....11.....',
    '..1811..1181....',
    '..11111111111...',
    '.1111111111111..',
    '.111441111441...',
    '.111451111451...',
    '.1111111711111..',
    '..11111111111...',
    '...111111111....',
    '..11111111111.1.',
    '..11111111111.1.',
    '..111..111..111.',
    '................',
    '................',
    '................',
  ],
  // idle_1: tail sways down 1px
  idle_1: [
    '................',
    '...11....11.....',
    '..1811..1181....',
    '..11111111111...',
    '.1111111111111..',
    '.111441111441...',
    '.111451111451...',
    '.1111111711111..',
    '..11111111111...',
    '...111111111....',
    '..11111111111...',
    '..11111111111.1.',
    '..111..111..1.1.',
    '................',
    '................',
    '................',
  ],

  // --- WALK: 4-frame leg cycle with head bob ---
  walk_0: [
    '................',
    '...11....11.....',
    '..1811..1181....',
    '..11111111111...',
    '.1111111111111..',
    '.111441111441...',
    '.111451111451...',
    '.1111111711111..',
    '..11111111111...',
    '...111111111.1..',
    '..11111111111...',
    '..11111111111...',
    '..1.1..1.1.11...',
    '................',
    '................',
    '................',
  ],
  walk_1: [
    '................',
    '................',
    '...11....11.....',
    '..1811..1181....',
    '..11111111111...',
    '.1111111111111..',
    '.111441111441...',
    '.111451111451...',
    '.1111111711111..',
    '..11111111111.1.',
    '...111111111.1..',
    '..11111111111...',
    '..11.1..11.1....',
    '................',
    '................',
    '................',
  ],
  walk_2: [
    '................',
    '...11....11.....',
    '..1811..1181....',
    '..11111111111...',
    '.1111111111111..',
    '.111441111441...',
    '.111451111451...',
    '.1111111711111..',
    '..11111111111...',
    '...111111111.1..',
    '..11111111111...',
    '..11111111111...',
    '...1.1..1.1.1...',
    '................',
    '................',
    '................',
  ],
  walk_3: [
    '................',
    '................',
    '...11....11.....',
    '..1811..1181....',
    '..11111111111...',
    '.1111111111111..',
    '.111441111441...',
    '.111451111451...',
    '.1111111711111..',
    '..11111111111.1.',
    '...111111111.1..',
    '..11111111111...',
    '..1.11..1.11....',
    '................',
    '................',
    '................',
  ],

  // --- SIT: lowered body, tucked legs ---
  sit_0: [
    '................',
    '................',
    '...11....11.....',
    '..1811..1181....',
    '..11111111111...',
    '.1111111111111..',
    '.111441111441...',
    '.111451111451...',
    '.1111111711111..',
    '..11111111111...',
    '..11111111111...',
    '..11111111111.1.',
    '.111111111111.1.',
    '.11..........1..',
    '................',
    '................',
  ],
  sit_1: [
    '................',
    '................',
    '...11....11.....',
    '..1811..1181....',
    '..11111111111...',
    '.1111111111111..',
    '.111441111441...',
    '.111451111451...',
    '.1111111711111..',
    '..11111111111...',
    '..11111111111...',
    '..11111111111...',
    '.111111111111.1.',
    '.11..........11.',
    '................',
    '................',
  ],

  // --- SLEEP: lying down, breathing animation ---
  sleep_0: [
    '................',
    '................',
    '................',
    '................',
    '................',
    '................',
    '................',
    '...11....11.....',
    '..1811..1181....',
    '..11111111111...',
    '.1111111111111..',
    '.111..1117.111..',
    '.1111111111111..',
    '.111111111111.1.',
    '..1111111111..1.',
    '................',
  ],
  sleep_1: [
    '................',
    '................',
    '................',
    '................',
    '................',
    '................',
    '................',
    '...11....11.....',
    '..1811..1181....',
    '..11111111111...',
    '.11111111111111.',
    '.111..1117.1111.',
    '.11111111111111.',
    '.1111111111111..',
    '..11111111111.1.',
    '................',
  ],

  // --- GROOM: paw raised to face ---
  groom_0: [
    '................',
    '...11....11.....',
    '..1811..1181....',
    '..11111111111...',
    '.1111111111111..',
    '.111441111441...',
    '.11145111.451...',
    '.111111171.11...',
    '..111.1111111...',
    '...1..111111....',
    '..11111111111.1.',
    '..11111111111.1.',
    '..111..111..111.',
    '................',
    '................',
    '................',
  ],
  groom_1: [
    '................',
    '...11....11.....',
    '..1811..1181....',
    '..11111111111...',
    '.1111111111111..',
    '.111441111441...',
    '.111451.1451....',
    '.1111117.111....',
    '..1111111.111...',
    '...111111..1....',
    '..11111111111.1.',
    '..11111111111.1.',
    '..111..111..111.',
    '................',
    '................',
    '................',
  ],
};

// ============================================================
// BREED PALETTES
// Each palette maps index characters to hex colors
// ============================================================

const BREED_PALETTES = {
  cat_orange_tabby: {
    '1': '#F0A050', '2': '#C87828', '3': '#F8C888',
    '4': '#FFFFFF', '5': '#2D3436', '6': '#1A1A1A',
    '7': '#FF8888', '8': '#FFB0B0',
    '9': '#F0A050', 'A': '#F0A050', 'B': '#D08030',
    stripes: true,
  },
  cat_black: {
    '1': '#404040', '2': '#303030', '3': '#505050',
    '4': '#FFD700', '5': '#1A1A1A', '6': '#0A0A0A',
    '7': '#808080', '8': '#FF9EAF',
    '9': '#404040', 'A': '#404040', 'B': '#303030',
  },
  cat_white: {
    '1': '#F0EDE8', '2': '#E0DDD8', '3': '#FFFFFF',
    '4': '#D0E8FF', '5': '#4488CC', '6': '#2266AA',
    '7': '#FF8888', '8': '#FFB0B0',
    '9': '#F0EDE8', 'A': '#F0EDE8', 'B': '#E0DDD8',
  },
  cat_calico: {
    '1': '#F0EDE8', '2': '#E0DDD8', '3': '#FFFFFF',
    '4': '#FFFFFF', '5': '#C8A030', '6': '#907020',
    '7': '#FF8888', '8': '#FFB0B0',
    '9': '#F0A050', 'A': '#505050', 'B': '#E0DDD8',
    patches: true,
  },
  cat_siamese: {
    '1': '#F0E0D0', '2': '#806050', '3': '#F8EDE0',
    '4': '#D0E8FF', '5': '#4488CC', '6': '#2266AA',
    '7': '#806050', '8': '#FF9EAF',
    '9': '#705040', 'A': '#705040', 'B': '#E0D0C0',
    points: true,
  },
  cat_russian_blue: {
    '1': '#8898A8', '2': '#788898', '3': '#98A8B8',
    '4': '#D0FFD0', '5': '#408040', '6': '#206020',
    '7': '#B0A0B8', '8': '#C0B0C8',
    '9': '#8898A8', 'A': '#8898A8', 'B': '#788898',
  },
  cat_tuxedo: {
    '1': '#404040', '2': '#303030', '3': '#505050',
    '4': '#FFFFFF', '5': '#508050', '6': '#306030',
    '7': '#FF8888', '8': '#FF9EAF',
    '9': '#F0EDE8', 'A': '#F0EDE8', 'B': '#303030',
    tuxedo: true,
  },
  cat_gray_tabby: {
    '1': '#A0A0A0', '2': '#707070', '3': '#B8B8B8',
    '4': '#FFFFFF', '5': '#2D3436', '6': '#1A1A1A',
    '7': '#FF8888', '8': '#FFB0B0',
    '9': '#A0A0A0', 'A': '#A0A0A0', 'B': '#808080',
    stripes: true,
  },
};

// ============================================================
// BREED-SPECIFIC OVERLAY FUNCTIONS
// Apply special markings (stripes, patches, tuxedo, points)
// ============================================================

function applyBreedOverlays(grid, breedType, palette) {
  // grid is a 16x16 2D array of characters
  // We modify certain cells based on breed-specific markings

  if (palette.stripes) {
    // Add stripe marks at forehead and body (matching SVG positions)
    const stripePositions = [
      // Forehead stripes (row where head top is)
      // Find the first row that has '1' characters for the head top
    ];
    // Apply stripes to specific positions in the grid
    for (let y = 0; y < 16; y++) {
      for (let x = 0; x < 16; x++) {
        if (grid[y][x] === '1') {
          // Forehead area stripes
          if (y >= 2 && y <= 3 && (x === 5 || x === 7 || x === 9)) {
            grid[y][x] = '2';
          }
          // Body stripes
          if (y >= 9 && y <= 10 && (x === 4 || x === 7 || x === 10)) {
            grid[y][x] = '2';
          }
        }
      }
    }
  }

  if (palette.patches) {
    // Calico: left side = patch1 (orange '9'), right side = patch2 (dark 'A')
    for (let y = 0; y < 16; y++) {
      for (let x = 0; x < 16; x++) {
        if (grid[y][x] === '1') {
          // Left ear and left head patch
          if (y <= 1 && x <= 5) grid[y][x] = '9';
          if (y >= 2 && y <= 4 && x <= 3) grid[y][x] = '9';
          // Right ear and right head patch
          if (y <= 1 && x >= 9) grid[y][x] = 'A';
          if (y >= 2 && y <= 4 && x >= 10) grid[y][x] = 'A';
          // Left body patch
          if (y >= 8 && y <= 11 && x <= 4) grid[y][x] = '9';
          // Right body patch
          if (y >= 9 && y <= 11 && x >= 9 && x <= 11) grid[y][x] = 'A';
        }
      }
    }
  }

  if (palette.tuxedo) {
    // White face marking + white bib
    for (let y = 0; y < 16; y++) {
      for (let x = 0; x < 16; x++) {
        if (grid[y][x] === '1') {
          // White chin/lower face
          if (y >= 5 && y <= 7 && x >= 5 && x <= 9) grid[y][x] = '9';
          if (y === 4 && x >= 6 && x <= 8) grid[y][x] = '9';
          // White bib on chest
          if (y === 8 && x >= 5 && x <= 9) grid[y][x] = '9';
          // White belly
          if (y >= 9 && y <= 10 && x >= 4 && x <= 10) grid[y][x] = '9';
          // White paws
          if (y >= 11 && y <= 12) grid[y][x] = '9';
        }
      }
    }
  }

  if (palette.points) {
    // Siamese: dark ears, face mask, paws, tail
    for (let y = 0; y < 16; y++) {
      for (let x = 0; x < 16; x++) {
        if (grid[y][x] === '1') {
          // Dark ears (already have ear positions)
          if (y <= 1) grid[y][x] = '9';
          // Dark face mask (around nose)
          if (y >= 5 && y <= 7 && x >= 6 && x <= 8) grid[y][x] = '2';
          if (y === 4 && x === 7) grid[y][x] = '2';
          // Dark paws
          if (y >= 11 && y <= 12 && (x <= 4 || x >= 10)) grid[y][x] = '9';
          // Dark tail
          if (y >= 7 && x >= 13) grid[y][x] = '9';
        }
      }
    }
  }
}

// ============================================================
// SVG GENERATION
// ============================================================

function generateCatSVG(frameKey, breedType) {
  const template = FRAME_TEMPLATES[frameKey];
  const palette = BREED_PALETTES[breedType];
  if (!template || !palette) return '';

  // Convert template strings to 2D char array for modification
  const grid = template.map(row => row.split(''));

  // Apply breed-specific overlays
  applyBreedOverlays(grid, breedType, palette);

  // Build SVG rects
  let rects = '';
  for (let y = 0; y < 16; y++) {
    for (let x = 0; x < 16; x++) {
      const ch = grid[y][x];
      if (ch === '.') continue;

      let color;
      if (ch === '8') {
        color = palette['8'];
      } else {
        color = palette[ch];
      }
      if (!color) continue;

      rects += `<rect x="${x}" y="${y}" width="1" height="1" fill="${color}"/>`;
    }
  }

  const svg = `<svg viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">${rects}</svg>`;
  return 'data:image/svg+xml,' + encodeURIComponent(svg);
}

// ============================================================
// SPRITE CACHE
// ============================================================

const SPRITE_CACHE = {};

function preRenderAllSprites() {
  const breeds = Object.keys(BREED_PALETTES);
  const frames = Object.keys(FRAME_TEMPLATES);
  for (const breed of breeds) {
    for (const frame of frames) {
      const key = breed + ':' + frame;
      SPRITE_CACHE[key] = generateCatSVG(frame, breed);
    }
  }
}

function getCachedSprite(breed, frame) {
  const key = breed + ':' + frame;
  if (SPRITE_CACHE[key]) return SPRITE_CACHE[key];
  // Fallback: generate on the fly
  const uri = generateCatSVG(frame, breed);
  SPRITE_CACHE[key] = uri;
  return uri;
}

// ============================================================
// ANIMATION SEQUENCES
// ============================================================

const ANIM_SEQUENCES = {
  idle:  { frames: ['idle_0', 'idle_1'], frameDuration: 800 },
  walk:  { frames: ['walk_0', 'walk_1', 'walk_2', 'walk_3'], frameDuration: 150 },
  sit:   { frames: ['sit_0', 'sit_1'], frameDuration: 1000 },
  sleep: { frames: ['sleep_0', 'sleep_1'], frameDuration: 1000 },
  groom: { frames: ['groom_0', 'groom_1'], frameDuration: 400 },
};

// Pre-render all sprites on load
preRenderAllSprites();
