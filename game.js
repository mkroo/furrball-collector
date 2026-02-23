// ============================================================
// CONFIG
// ============================================================
const CONFIG = {
  GACHA_COST: 10,
  CAT_SPEED: 0.6,            // pixels per frame
  FURBALL_DROP_MIN: 4000,     // ms
  FURBALL_DROP_MAX: 10000,    // ms
  FURBALL_LIFETIME: 15000,    // ms before furball disappears
  CAT_IDLE_MIN: 2000,
  CAT_IDLE_MAX: 5000,
  SAVE_INTERVAL: 15000,
  SPRITE_SIZE: 64,
  FURBALL_SIZE: 40,
};

// ============================================================
// XP CONFIG (Feature #6)
// ============================================================
const XP_SOURCES = {
  COLLECT_FURBALL: 1,
  ROLL_GACHA: 5,
  PLACE_ITEM: 10,
  PLACE_EPIC_ITEM: 25,
};

const SHELTER_LEVELS = [
  { level: 1,  name: '빈 공터',       xpNeeded: 0,    cats: ['cat_orange_tabby', 'cat_black'] },
  { level: 2,  name: '작은 마당',     xpNeeded: 50,   cats: ['cat_white'] },
  { level: 3,  name: '쉼터 터전',     xpNeeded: 150,  cats: ['cat_gray_tabby'] },
  { level: 4,  name: '아늑한 쉼터',   xpNeeded: 300,  cats: ['cat_calico'] },
  { level: 5,  name: '인기 쉼터',     xpNeeded: 500,  cats: ['cat_siamese'] },
  { level: 6,  name: '고양이 놀이터', xpNeeded: 800,  cats: [] },
  { level: 7,  name: '고양이 카페',   xpNeeded: 1200, cats: ['cat_russian_blue'] },
  { level: 8,  name: '고양이 왕국',   xpNeeded: 1800, cats: [] },
  { level: 9,  name: '고양이 낙원',   xpNeeded: 2500, cats: ['cat_tuxedo'] },
  { level: 10, name: '고양이 천국',   xpNeeded: 3500, cats: [] },
];

const CAT_NAMES = {
  cat_orange_tabby: '치즈',
  cat_black:        '까망',
  cat_white:        '하양',
  cat_gray_tabby:   '줄무늬',
  cat_calico:       '삼색',
  cat_siamese:      '샴',
  cat_russian_blue: '블루',
  cat_tuxedo:       '턱시도',
};

const FURBALL_TYPES = [
  'furball_orange', 'furball_black', 'furball_white',
  'furball_gray', 'furball_calico', 'furball_golden',
];

const CAT_TO_FURBALL = {
  cat_orange_tabby: 'furball_orange',
  cat_black:        'furball_black',
  cat_white:        'furball_white',
  cat_gray_tabby:   'furball_gray',
  cat_calico:       'furball_calico',
  cat_siamese:      'furball_calico',
  cat_russian_blue: 'furball_gray',
  cat_tuxedo:       'furball_black',
};

const GACHA_ITEMS = {
  traffic_cone:    { name: '라바콘',       desc: '어디서 가져온 걸까...?',           rarity: 'common', img: 'assets/gacha_items/traffic_cone.png' },
  cardboard_box:   { name: '택배 상자',    desc: '고양이가 제일 좋아하는 가구',      rarity: 'common', img: 'assets/gacha_items/cardboard_box.png' },
  cushion:         { name: '쿠션',         desc: '폭신폭신 낮잠 천국',               rarity: 'common', img: 'assets/gacha_items/cushion.png' },
  food_bowl:       { name: '밥그릇',       desc: '맛있는 밥이 가득',                 rarity: 'common', img: 'assets/gacha_items/food_bowl.png' },
  yarn_ball:       { name: '털실 뭉치',    desc: '끝없는 재미의 원천',               rarity: 'rare',   img: 'assets/gacha_items/yarn_ball.png' },
  fish_toy:        { name: '물고기 장난감', desc: '진짜 물고기 아님 주의',            rarity: 'rare',   img: 'assets/gacha_items/fish_toy.png' },
  mouse_toy:       { name: '쥐 장난감',    desc: '삑삑! 소리가 나요',                rarity: 'rare',   img: 'assets/gacha_items/mouse_toy.png' },
  plant_pot:       { name: '화분',         desc: '가끔 흙을 파는 고양이 주의',       rarity: 'rare',   img: 'assets/gacha_items/plant_pot.png' },
  cat_tower:       { name: '캣타워',       desc: '고양이들의 꿈의 놀이터!',          rarity: 'epic',   img: 'assets/gacha_items/cat_tower.png' },
  trash_can:       { name: '쓰레기통',     desc: '생선뼈 냄새가 솔솔~',              rarity: 'epic',   img: 'assets/gacha_items/trash_can.png' },
  scratching_post: { name: '스크래처',     desc: '가구 대신 이걸 긁어주세요',        rarity: 'epic',   img: 'assets/gacha_items/scratching_post.png' },
  window_perch:    { name: '창문 선반',    desc: '바깥 구경 최고의 자리',            rarity: 'epic',   img: 'assets/gacha_items/window_perch.png' },
};

const RARITY_WEIGHTS = { common: 50, rare: 35, epic: 15 };
const RARITY_LABELS = { common: '일반', rare: '레어', epic: '에픽' };

// ============================================================
// ACHIEVEMENTS (Feature #3)
// ============================================================
const ACHIEVEMENTS = [
  { id: 'first_furball',    name: '첫 털뭉치',       desc: '처음으로 털뭉치를 수집했다!',     icon: '🧶', hidden: false, check: (s) => s.furballsCollected >= 1 },
  { id: 'furball_100',      name: '수집왕',           desc: '털뭉치 100개 수집!',              icon: '🏆', hidden: false, check: (s) => s.furballsCollected >= 100 },
  { id: 'furball_1000',     name: '전설의 수집가',    desc: '털뭉치 1000개 수집!',             icon: '👑', hidden: true,  check: (s) => s.furballsCollected >= 1000 },
  { id: 'first_gacha',      name: '첫 가챠',          desc: '처음으로 냥챠를 돌렸다!',         icon: '🎰', hidden: false, check: (s) => s.gachaRollCount >= 1 },
  { id: 'gacha_10',         name: '가챠 매니아',      desc: '냥챠 10회 돌리기!',               icon: '🎪', hidden: false, check: (s) => s.gachaRollCount >= 10 },
  { id: 'first_epic',       name: '에픽 등장!',       desc: '에픽 아이템을 획득했다!',         icon: '💎', hidden: false, check: (s) => s.epicItemsObtained >= 1 },
  { id: 'level_5',          name: '인기 쉼터',        desc: '쉼터 레벨 5 달성!',               icon: '⭐', hidden: false, check: (s) => s.shelterLevel >= 5 },
  { id: 'level_max',        name: '고양이 천국',      desc: '최고 레벨 달성!',                 icon: '🌟', hidden: true,  check: (s) => s.shelterLevel >= 10 },
  { id: 'items_25',         name: '인테리어 장인',    desc: '아이템 25개 배치!',               icon: '🏠', hidden: false, check: (s) => s.totalItemsPlaced >= 25 },
  { id: 'first_name',       name: '이름 지어주기',    desc: '고양이에게 이름을 지어줬다!',     icon: '📝', hidden: false, check: (s) => Object.keys(s.catNames).length >= 1 },
  { id: 'all_names',        name: '작명 마스터',      desc: '모든 고양이에게 이름을 지어줬다!',icon: '✏️', hidden: true,  check: (s) => Object.keys(s.catNames).length >= Object.keys(CAT_NAMES).length },
  { id: 'full_collection',  name: '도감 완성',        desc: '모든 고양이가 쉼터를 찾아왔다!',  icon: '📖', hidden: true,  check: (s) => { const u = getUnlockedCats(); return u.length >= Object.keys(CAT_NAMES).length; } },
  { id: 'gacha_50',         name: '가챠 마스터',      desc: '냥챠 50회 돌리기!',               icon: '🎯', hidden: true,  check: (s) => s.gachaRollCount >= 50 },
  { id: 'xp_1000',          name: '경험치 부자',      desc: 'XP 1000 달성!',                   icon: '💫', hidden: false, check: (s) => s.xp >= 1000 },
];

// ============================================================
// GAME STATE
// ============================================================
let state = {
  furballs: 0,
  inventory: {},       // { itemId: count }
  placedItems: [],     // [{ id, type, x, y }] positions in % of field
  shelterLevel: 1,
  totalItemsPlaced: 0,
  started: false,
  // Feature #7: speed control
  catSpeedMultiplier: 1.0,
  // Feature #5: cat names
  catNames: {},
  // Feature #6: XP system
  xp: 0,
  gachaRollCount: 0,
  furballsCollected: 0,
  // Feature #3: achievements
  unlockedAchievements: [],
  epicItemsObtained: 0,
};

let nextItemId = 1;
let isViewMode = false;  // Feature #2: shelter visit

// ============================================================
// DOM REFS
// ============================================================
const $ = (sel) => document.querySelector(sel);
const field = $('#game-field');
const introOverlay = $('#intro-overlay');
const gachaModal = $('#gacha-modal');

// ============================================================
// RUNTIME
// ============================================================
let cats = [];            // active Cat instances
let droppedFurballs = []; // active furball elements on field
let selectedInventoryItem = null;
let placementGhost = null;
let lastTime = 0;
let saveTimer = 0;

// ============================================================
// CAT CLASS
// ============================================================
class Cat {
  constructor(type) {
    this.type = type;
    this.el = document.createElement('img');
    this.el.src = `assets/cats/${type}.svg`;
    this.el.className = 'cat-sprite';
    this.el.alt = CAT_NAMES[type] || type;

    const rect = field.getBoundingClientRect();
    this.x = Math.random() * (rect.width - CONFIG.SPRITE_SIZE);
    this.y = 100 + Math.random() * (rect.height - CONFIG.SPRITE_SIZE - 120);

    this.targetX = this.x;
    this.targetY = this.y;
    this.state = 'idle'; // idle | walking | dropping
    this.stateTimer = this._randomIdle();
    this.dropTimer = this._randomDropTime();
    this.facingRight = true;

    // Feature #5: name label
    this.nameEl = document.createElement('div');
    this.nameEl.className = 'cat-name-label';
    this._updateNameLabel();
    field.appendChild(this.nameEl);

    this._updatePosition();
    field.appendChild(this.el);
  }

  _updateNameLabel() {
    const customName = state.catNames[this.type];
    this.nameEl.textContent = customName || CAT_NAMES[this.type] || this.type;
  }

  _randomIdle() {
    return CONFIG.CAT_IDLE_MIN + Math.random() * (CONFIG.CAT_IDLE_MAX - CONFIG.CAT_IDLE_MIN);
  }

  _randomDropTime() {
    const mult = state.catSpeedMultiplier || 1.0;
    const base = CONFIG.FURBALL_DROP_MIN + Math.random() * (CONFIG.FURBALL_DROP_MAX - CONFIG.FURBALL_DROP_MIN);
    return base / mult;
  }

  _pickTarget() {
    const rect = field.getBoundingClientRect();
    this.targetX = 20 + Math.random() * (rect.width - CONFIG.SPRITE_SIZE - 40);
    this.targetY = 80 + Math.random() * (rect.height - CONFIG.SPRITE_SIZE - 100);
  }

  _updatePosition() {
    this.el.style.left = this.x + 'px';
    this.el.style.top = this.y + 'px';
    this.el.style.transform = this.facingRight ? 'scaleX(1)' : 'scaleX(-1)';
    // Sync name label position (centered above cat)
    this.nameEl.style.left = (this.x + CONFIG.SPRITE_SIZE / 2) + 'px';
    this.nameEl.style.top = (this.y - 18) + 'px';
  }

  update(dt) {
    this.stateTimer -= dt;
    if (!isViewMode) {
      this.dropTimer -= dt;
      if (this.dropTimer <= 0) {
        this._dropFurball();
        this.dropTimer = this._randomDropTime();
      }
    }

    const speedMult = state.catSpeedMultiplier || 1.0;

    if (this.state === 'idle') {
      if (this.stateTimer <= 0) {
        this._pickTarget();
        this.state = 'walking';
      }
    } else if (this.state === 'walking') {
      const dx = this.targetX - this.x;
      const dy = this.targetY - this.y;
      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < 2) {
        this.x = this.targetX;
        this.y = this.targetY;
        this.state = 'idle';
        this.stateTimer = this._randomIdle();
      } else {
        const speed = CONFIG.CAT_SPEED * speedMult * (dt / 16);
        this.x += (dx / dist) * speed * 2;
        this.y += (dy / dist) * speed * 2;
        this.facingRight = dx >= 0;
      }
    }

    this._updatePosition();
  }

  _dropFurball() {
    const furballType = CAT_TO_FURBALL[this.type] || 'furball_orange';
    spawnFurball(this.x + CONFIG.SPRITE_SIZE / 2, this.y + CONFIG.SPRITE_SIZE - 10, furballType);
  }

  destroy() {
    this.el.remove();
    this.nameEl.remove();
  }
}

// ============================================================
// FURBALL SYSTEM
// ============================================================
function spawnFurball(x, y, type) {
  const el = document.createElement('img');
  el.src = `assets/furballs/${type}.png`;
  el.className = 'furball-sprite';
  el.style.left = (x - CONFIG.FURBALL_SIZE / 2) + 'px';
  el.style.top = y + 'px';

  const furball = { el, x, y, type, born: Date.now() };

  el.addEventListener('click', (e) => {
    e.stopPropagation();
    collectFurball(furball);
  });

  field.appendChild(el);
  droppedFurballs.push(furball);
}

function collectFurball(furball) {
  state.furballs++;
  state.furballsCollected++;
  addXP(XP_SOURCES.COLLECT_FURBALL, furball.x, furball.y);
  showFloatText(furball.x, furball.y, '+1');
  showSparkles(furball.x, furball.y);
  furball.el.style.transition = 'transform 0.2s, opacity 0.2s';
  furball.el.style.transform = 'scale(1.5)';
  furball.el.style.opacity = '0';

  setTimeout(() => {
    furball.el.remove();
  }, 200);

  droppedFurballs = droppedFurballs.filter(f => f !== furball);
  updateUI();
  checkAchievements();
}

function showSparkles(x, y) {
  const symbols = ['\u2728', '\u2764', '\u2B50', '\u2740'];
  for (let i = 0; i < 5; i++) {
    const el = document.createElement('div');
    el.className = 'sparkle';
    el.textContent = symbols[Math.floor(Math.random() * symbols.length)];
    el.style.left = (x + (Math.random() - 0.5) * 40) + 'px';
    el.style.top = (y + (Math.random() - 0.5) * 30) + 'px';
    el.style.animationDelay = (Math.random() * 0.3) + 's';
    field.appendChild(el);
    setTimeout(() => el.remove(), 1200);
  }
}

function updateFurballs() {
  const now = Date.now();
  droppedFurballs = droppedFurballs.filter(f => {
    if (now - f.born > CONFIG.FURBALL_LIFETIME) {
      f.el.style.transition = 'opacity 0.5s';
      f.el.style.opacity = '0';
      setTimeout(() => f.el.remove(), 500);
      return false;
    }
    return true;
  });
}

// ============================================================
// FLOAT TEXT
// ============================================================
function showFloatText(x, y, text) {
  const el = document.createElement('div');
  el.className = 'float-text';
  el.textContent = text;
  el.style.left = x + 'px';
  el.style.top = y + 'px';
  field.appendChild(el);
  setTimeout(() => el.remove(), 1000);
}

// ============================================================
// XP SYSTEM (Feature #6)
// ============================================================
function addXP(amount, x, y) {
  state.xp += amount;
  if (x !== undefined && y !== undefined) {
    showFloatText(x + 20, y - 15, `+${amount} XP`);
  }
  checkLevelUp();
}

// ============================================================
// GACHA SYSTEM
// ============================================================
function rollGacha() {
  if (state.furballs < CONFIG.GACHA_COST) return;

  state.furballs -= CONFIG.GACHA_COST;
  state.gachaRollCount++;
  updateUI();

  // Pick rarity
  const roll = Math.random() * 100;
  let rarity;
  if (roll < RARITY_WEIGHTS.common) rarity = 'common';
  else if (roll < RARITY_WEIGHTS.common + RARITY_WEIGHTS.rare) rarity = 'rare';
  else rarity = 'epic';

  // Pick item of that rarity
  const pool = Object.entries(GACHA_ITEMS).filter(([, v]) => v.rarity === rarity);
  const [itemId, itemData] = pool[Math.floor(Math.random() * pool.length)];

  // Add to inventory
  state.inventory[itemId] = (state.inventory[itemId] || 0) + 1;

  // Track epic
  if (rarity === 'epic') {
    state.epicItemsObtained++;
  }

  // Add XP
  addXP(XP_SOURCES.ROLL_GACHA);

  // Show modal
  showGachaResult(itemId, itemData, rarity);
  checkAchievements();
  saveGame();
}

function showGachaResult(itemId, itemData, rarity) {
  gachaModal.classList.remove('hidden');

  const capsule = $('#gacha-capsule');
  const reveal = $('#gacha-reveal');
  reveal.classList.add('hidden');

  capsule.className = 'gacha-capsule capsule-' + rarity;
  capsule.style.display = 'block';

  setTimeout(() => {
    capsule.style.display = 'none';
    reveal.classList.remove('hidden');

    const badge = $('#rarity-badge');
    badge.className = 'rarity-badge rarity-' + rarity;
    badge.textContent = RARITY_LABELS[rarity];

    $('#gacha-item-img').src = itemData.img;
    $('#gacha-item-name').textContent = itemData.name;
    $('#gacha-item-desc').textContent = itemData.desc;
  }, 900);
}

function closeGachaModal() {
  gachaModal.classList.add('hidden');
  updateInventoryUI();
}

// ============================================================
// INVENTORY & PLACEMENT
// ============================================================
function updateInventoryUI() {
  const inv = $('#inventory');
  inv.innerHTML = '';

  const entries = Object.entries(state.inventory).filter(([, count]) => count > 0);

  if (entries.length === 0) {
    inv.innerHTML = '<p style="grid-column:1/-1; text-align:center; color:#666; font-size:12px;">아직 아이템이 없습니다</p>';
    return;
  }

  for (const [itemId, count] of entries) {
    const data = GACHA_ITEMS[itemId];
    if (!data) continue;

    const slot = document.createElement('div');
    slot.className = 'inventory-slot';
    if (selectedInventoryItem === itemId) slot.classList.add('selected');
    slot.title = `${data.name} (${RARITY_LABELS[data.rarity]})`;

    const img = document.createElement('img');
    img.src = data.img;
    img.alt = data.name;
    slot.appendChild(img);

    if (count > 1) {
      const badge = document.createElement('div');
      badge.className = 'count-badge';
      badge.textContent = count;
      slot.appendChild(badge);
    }

    const rarityDot = document.createElement('div');
    rarityDot.className = 'rarity-indicator';
    rarityDot.textContent = data.rarity === 'epic' ? '★★★' : data.rarity === 'rare' ? '★★' : '★';
    slot.appendChild(rarityDot);

    slot.addEventListener('click', () => {
      if (selectedInventoryItem === itemId) {
        cancelPlacement();
      } else {
        selectForPlacement(itemId);
      }
    });

    inv.appendChild(slot);
  }
}

function selectForPlacement(itemId) {
  selectedInventoryItem = itemId;
  updateInventoryUI();
  $('#placement-hint').style.display = 'block';
  field.style.cursor = 'crosshair';

  // Create ghost
  if (placementGhost) placementGhost.remove();
  placementGhost = document.createElement('img');
  placementGhost.src = GACHA_ITEMS[itemId].img;
  placementGhost.className = 'placement-ghost';
  field.appendChild(placementGhost);
}

function cancelPlacement() {
  selectedInventoryItem = null;
  if (placementGhost) { placementGhost.remove(); placementGhost = null; }
  $('#placement-hint').style.display = 'none';
  field.style.cursor = 'default';
  updateInventoryUI();
}

function placeItem(itemId, fieldX, fieldY) {
  const rect = field.getBoundingClientRect();
  const xPercent = ((fieldX - CONFIG.SPRITE_SIZE / 2) / rect.width) * 100;
  const yPercent = ((fieldY - CONFIG.SPRITE_SIZE / 2) / rect.height) * 100;

  // Clamp
  const xClamped = Math.max(0, Math.min(xPercent, 100 - (CONFIG.SPRITE_SIZE / rect.width) * 100));
  const yClamped = Math.max(5, Math.min(yPercent, 100 - (CONFIG.SPRITE_SIZE / rect.height) * 100));

  const item = {
    id: nextItemId++,
    type: itemId,
    x: xClamped,
    y: yClamped,
  };

  state.placedItems.push(item);
  state.inventory[itemId]--;
  if (state.inventory[itemId] <= 0) delete state.inventory[itemId];
  state.totalItemsPlaced = state.placedItems.length;

  // XP based on rarity
  const itemData = GACHA_ITEMS[itemId];
  const xpAmount = (itemData && itemData.rarity === 'epic') ? XP_SOURCES.PLACE_EPIC_ITEM : XP_SOURCES.PLACE_ITEM;
  addXP(xpAmount);

  renderPlacedItem(item);
  cancelPlacement();
  checkLevelUp();
  updateUI();
  checkAchievements();
  saveGame();
}

function renderPlacedItem(item) {
  const data = GACHA_ITEMS[item.type];
  if (!data) return;

  const el = document.createElement('img');
  el.src = data.img;
  el.className = 'placed-item-sprite';
  el.style.left = item.x + '%';
  el.style.top = item.y + '%';
  el.title = `${data.name} - 클릭하면 회수`;
  el.dataset.itemId = item.id;

  el.addEventListener('click', (e) => {
    if (selectedInventoryItem) return; // Don't pick up while placing
    if (isViewMode) return; // Read-only in view mode
    e.stopPropagation();
    pickUpItem(item, el);
  });

  field.appendChild(el);
}

function pickUpItem(item, el) {
  // Return to inventory
  state.inventory[item.type] = (state.inventory[item.type] || 0) + 1;
  state.placedItems = state.placedItems.filter(i => i.id !== item.id);
  state.totalItemsPlaced = state.placedItems.length;

  el.style.transition = 'transform 0.2s, opacity 0.2s';
  el.style.transform = 'scale(0.5)';
  el.style.opacity = '0';
  setTimeout(() => el.remove(), 200);

  showToast(`${GACHA_ITEMS[item.type].name}을(를) 회수했습니다`);
  checkLevelUp();
  updateUI();
  saveGame();
}

function renderAllPlacedItems() {
  document.querySelectorAll('.placed-item-sprite').forEach(el => el.remove());
  for (const item of state.placedItems) {
    renderPlacedItem(item);
  }
}

// ============================================================
// SHELTER LEVEL (XP-based, Feature #6)
// ============================================================
function getUnlockedCats() {
  const unlocked = [];
  for (const level of SHELTER_LEVELS) {
    if (level.level <= state.shelterLevel) {
      unlocked.push(...level.cats);
    }
  }
  return unlocked;
}

function getCurrentLevelData() {
  return SHELTER_LEVELS.find(l => l.level === state.shelterLevel) || SHELTER_LEVELS[0];
}

function getNextLevelData() {
  return SHELTER_LEVELS.find(l => l.level === state.shelterLevel + 1);
}

function checkLevelUp() {
  const prev = state.shelterLevel;
  let newLevel = 1;
  for (const level of SHELTER_LEVELS) {
    if (state.xp >= level.xpNeeded) {
      newLevel = level.level;
    }
  }

  state.shelterLevel = newLevel;

  if (newLevel > prev) {
    const levelData = SHELTER_LEVELS.find(l => l.level === newLevel);
    showToast(`쉼터가 레벨업! Lv.${newLevel} "${levelData.name}"`);

    // Level-up bonus: grant furballs
    const bonus = newLevel * 3;
    state.furballs += bonus;
    showToast(`레벨업 보상: 털뭉치 ${bonus}개!`);

    for (const catType of levelData.cats) {
      showToast(`새로운 고양이 "${CAT_NAMES[catType]}"이(가) 찾아왔어요!`);
    }

    syncCats();
    checkAchievements();
  } else if (newLevel < prev) {
    syncCats();
  }

  updateFieldBackground();
  updateCatListUI();
}

function updateFieldBackground() {
  field.className = 'field-level-' + state.shelterLevel;
}

// ============================================================
// CAT MANAGEMENT
// ============================================================
function syncCats() {
  const unlocked = getUnlockedCats();

  // Remove cats that are no longer unlocked
  cats = cats.filter(cat => {
    if (!unlocked.includes(cat.type)) {
      cat.destroy();
      return false;
    }
    return true;
  });

  // Add new cats
  const existingTypes = new Set(cats.map(c => c.type));
  for (const type of unlocked) {
    if (!existingTypes.has(type)) {
      cats.push(new Cat(type));
    }
  }
}

function refreshCatNames() {
  for (const cat of cats) {
    cat._updateNameLabel();
  }
}

// ============================================================
// UI UPDATES
// ============================================================
function updateUI() {
  // Furball count
  $('#furball-count').textContent = state.furballs;
  $('#sidebar-furball-count').textContent = state.furballs;

  // Gacha button
  const btn = $('#gacha-btn');
  btn.disabled = state.furballs < CONFIG.GACHA_COST;

  // Level bar (XP-based)
  const currentLevel = getCurrentLevelData();
  const nextLevel = getNextLevelData();
  $('#shelter-name').textContent = currentLevel.name;

  if (nextLevel) {
    const currentXP = state.xp - currentLevel.xpNeeded;
    const xpRange = nextLevel.xpNeeded - currentLevel.xpNeeded;
    const progress = Math.min((currentXP / xpRange) * 100, 100);
    $('#level-fill').style.width = progress + '%';
    $('#level-text').textContent = `Lv.${state.shelterLevel} (${state.xp}/${nextLevel.xpNeeded} XP)`;
  } else {
    $('#level-fill').style.width = '100%';
    $('#level-text').textContent = `Lv.${state.shelterLevel} MAX`;
  }

  updateInventoryUI();
  updateCatListUI();
  updateAchievementUI();
}

function updateCatListUI() {
  const list = $('#cat-list');
  list.innerHTML = '';
  const allCats = Object.keys(CAT_NAMES);
  const unlocked = getUnlockedCats();

  for (const catType of allCats) {
    const badge = document.createElement('div');
    badge.className = 'cat-badge';
    const isUnlocked = unlocked.includes(catType);
    if (!isUnlocked) badge.classList.add('locked');

    const img = document.createElement('img');
    img.src = `assets/cats/${catType}.svg`;
    img.alt = CAT_NAMES[catType];
    badge.appendChild(img);

    const displayName = state.catNames[catType] || CAT_NAMES[catType];
    badge.title = isUnlocked ? displayName : '???';

    // Feature #5: click to rename
    if (isUnlocked) {
      badge.addEventListener('click', () => openNameModal(catType));
    }

    list.appendChild(badge);
  }
}

// ============================================================
// CAT NAME MODAL (Feature #5)
// ============================================================
function openNameModal(catType) {
  const modal = $('#name-modal');
  modal.classList.remove('hidden');

  $('#name-modal-img').src = `assets/cats/${catType}.svg`;
  const defaultName = CAT_NAMES[catType];
  const currentName = state.catNames[catType] || defaultName;
  $('#name-modal-title').textContent = `${defaultName}의 이름`;
  $('#name-modal-input').value = currentName;
  $('#name-modal-input').focus();

  // Store which cat we're editing
  modal.dataset.catType = catType;
}

function confirmNameModal() {
  const modal = $('#name-modal');
  const catType = modal.dataset.catType;
  const input = $('#name-modal-input').value.trim().slice(0, 8);

  if (input && input !== CAT_NAMES[catType]) {
    state.catNames[catType] = input;
  } else if (!input || input === CAT_NAMES[catType]) {
    delete state.catNames[catType];
  }

  modal.classList.add('hidden');
  refreshCatNames();
  updateCatListUI();
  checkAchievements();
  saveGame();
}

function closeNameModal() {
  $('#name-modal').classList.add('hidden');
}

// ============================================================
// ACHIEVEMENTS (Feature #3)
// ============================================================
function checkAchievements() {
  for (const ach of ACHIEVEMENTS) {
    if (state.unlockedAchievements.includes(ach.id)) continue;
    if (ach.check(state)) {
      state.unlockedAchievements.push(ach.id);
      showAchievementToast(ach);
    }
  }
  updateAchievementUI();
}

function showAchievementToast(ach) {
  const container = $('#toast-container');
  const toast = document.createElement('div');
  toast.className = 'toast achievement-toast';
  toast.textContent = `${ach.icon} 업적 달성: ${ach.name}!`;
  container.appendChild(toast);
  setTimeout(() => toast.remove(), 3500);

  // Sparkle effect at center of screen
  const cx = window.innerWidth / 2;
  const cy = window.innerHeight / 3;
  for (let i = 0; i < 8; i++) {
    const el = document.createElement('div');
    el.className = 'sparkle';
    el.textContent = ['✨', '🌟', '⭐', '💫'][Math.floor(Math.random() * 4)];
    el.style.left = (cx + (Math.random() - 0.5) * 120) + 'px';
    el.style.top = (cy + (Math.random() - 0.5) * 60) + 'px';
    el.style.position = 'fixed';
    el.style.zIndex = '200';
    el.style.animationDelay = (Math.random() * 0.5) + 's';
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 1500);
  }
}

function updateAchievementUI() {
  const grid = $('#badge-grid');
  if (!grid) return;
  grid.innerHTML = '';

  for (const ach of ACHIEVEMENTS) {
    const badge = document.createElement('div');
    badge.className = 'achievement-badge';
    const isUnlocked = state.unlockedAchievements.includes(ach.id);

    if (isUnlocked) {
      badge.classList.add('unlocked');
      badge.textContent = ach.icon;
    } else {
      badge.classList.add('locked');
      badge.textContent = ach.hidden ? '?' : ach.icon;
    }

    // Tooltip
    const tooltip = document.createElement('div');
    tooltip.className = 'achievement-tooltip';
    if (isUnlocked) {
      tooltip.textContent = `${ach.name}: ${ach.desc}`;
    } else if (ach.hidden) {
      tooltip.textContent = '???';
    } else {
      tooltip.textContent = ach.name;
    }
    badge.appendChild(tooltip);

    grid.appendChild(badge);
  }
}

// ============================================================
// TOAST NOTIFICATIONS
// ============================================================
function showToast(message) {
  const container = $('#toast-container');
  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.textContent = message;
  container.appendChild(toast);
  setTimeout(() => toast.remove(), 3000);
}

// ============================================================
// SAVE / LOAD
// ============================================================
function saveGame() {
  if (isViewMode) return; // Don't save in view mode
  const data = {
    furballs: state.furballs,
    inventory: state.inventory,
    placedItems: state.placedItems,
    shelterLevel: state.shelterLevel,
    totalItemsPlaced: state.totalItemsPlaced,
    started: state.started,
    nextItemId: nextItemId,
    // Feature #7
    catSpeedMultiplier: state.catSpeedMultiplier,
    // Feature #5
    catNames: state.catNames,
    // Feature #6
    xp: state.xp,
    gachaRollCount: state.gachaRollCount,
    furballsCollected: state.furballsCollected,
    // Feature #3
    unlockedAchievements: state.unlockedAchievements,
    epicItemsObtained: state.epicItemsObtained,
  };
  localStorage.setItem('furrball-collector-save', JSON.stringify(data));
}

function loadGame() {
  const raw = localStorage.getItem('furrball-collector-save');
  if (!raw) return false;

  try {
    const data = JSON.parse(raw);
    state.furballs = data.furballs || 0;
    state.inventory = data.inventory || {};
    state.placedItems = data.placedItems || [];
    state.shelterLevel = data.shelterLevel || 1;
    state.totalItemsPlaced = data.totalItemsPlaced || 0;
    state.started = data.started || false;
    nextItemId = data.nextItemId || 1;

    // Feature #7
    state.catSpeedMultiplier = data.catSpeedMultiplier || 1.0;
    // Feature #5
    state.catNames = data.catNames || {};
    // Feature #6: XP migration
    if (data.xp !== undefined) {
      state.xp = data.xp;
    } else {
      // Migrate from old save: estimate XP from totalItemsPlaced
      state.xp = (data.totalItemsPlaced || 0) * 10;
    }
    state.gachaRollCount = data.gachaRollCount || 0;
    state.furballsCollected = data.furballsCollected || 0;
    // Feature #3
    state.unlockedAchievements = data.unlockedAchievements || [];
    state.epicItemsObtained = data.epicItemsObtained || 0;

    // Recalculate shelter level from XP
    let newLevel = 1;
    for (const level of SHELTER_LEVELS) {
      if (state.xp >= level.xpNeeded) {
        newLevel = level.level;
      }
    }
    state.shelterLevel = newLevel;

    return true;
  } catch {
    return false;
  }
}

// ============================================================
// SCREENSHOT SHARING (Feature #1)
// ============================================================
function captureAndShare() {
  if (typeof html2canvas === 'undefined') {
    showToast('스크린샷 기능을 불러오는 중...');
    return;
  }

  showToast('스크린샷 생성 중...');

  // Create a card canvas
  const card = document.createElement('div');
  card.style.cssText = `
    position: fixed; top: -9999px; left: -9999px;
    width: 1080px; height: 1920px;
    background: linear-gradient(180deg, #FFF0F5 0%, #FFE8EF 100%);
    display: flex; flex-direction: column; align-items: center;
    font-family: 'Jua', sans-serif; overflow: hidden;
  `;

  // Title area
  const titleArea = document.createElement('div');
  titleArea.style.cssText = 'padding: 80px 40px 40px; text-align: center; width: 100%;';
  titleArea.innerHTML = `
    <div style="font-size: 64px; color: #FF6B8A; font-weight: bold; text-shadow: 2px 2px 0 rgba(255,183,193,0.5);">냥줍쉼터</div>
    <div style="font-size: 32px; color: #8B7DA0; margin-top: 16px;">Lv.${state.shelterLevel} ${getCurrentLevelData().name}</div>
    <div style="font-size: 28px; color: #FFB347; margin-top: 8px;">고양이 ${getUnlockedCats().length}마리 | 업적 ${state.unlockedAchievements.length}개</div>
  `;
  card.appendChild(titleArea);

  // Game field snapshot
  html2canvas(field, {
    backgroundColor: null,
    scale: 2,
    useCORS: true,
    allowTaint: true,
  }).then(fieldCanvas => {
    const fieldImg = document.createElement('img');
    fieldImg.src = fieldCanvas.toDataURL();
    fieldImg.style.cssText = 'width: 960px; height: 1200px; object-fit: cover; border-radius: 24px; border: 4px solid #FFD1DC; margin: 20px 0;';
    card.appendChild(fieldImg);

    // Footer
    const footer = document.createElement('div');
    footer.style.cssText = 'padding: 40px; text-align: center; width: 100%;';
    footer.innerHTML = `
      <div style="font-size: 28px; color: #FF6B8A; margin-bottom: 16px;">같이 놀자! 🐱</div>
      <div style="font-size: 22px; color: #B0A0B8;">furrball-collector</div>
    `;
    card.appendChild(footer);

    document.body.appendChild(card);

    html2canvas(card, {
      width: 1080,
      height: 1920,
      scale: 1,
      useCORS: true,
      allowTaint: true,
    }).then(canvas => {
      card.remove();

      canvas.toBlob(async (blob) => {
        if (!blob) {
          showToast('이미지 생성에 실패했습니다');
          return;
        }

        // Try Web Share API (mobile)
        if (navigator.share && navigator.canShare) {
          const file = new File([blob], 'my-shelter.png', { type: 'image/png' });
          const shareData = { files: [file], title: '냥줍쉼터', text: '내 냥줍쉼터를 구경해봐!' };
          if (navigator.canShare(shareData)) {
            try {
              await navigator.share(shareData);
              showToast('공유 완료!');
              return;
            } catch (e) {
              if (e.name === 'AbortError') return;
            }
          }
        }

        // Desktop fallback: show preview + download
        showSharePreview(canvas);
      }, 'image/png');
    });
  });
}

function showSharePreview(canvas) {
  const overlay = $('#share-card-overlay');
  overlay.classList.remove('hidden');

  const container = overlay.querySelector('.share-card-container');
  // Remove old preview image if exists
  const oldImg = container.querySelector('.share-card-preview');
  if (oldImg) oldImg.remove();

  const img = document.createElement('img');
  img.src = canvas.toDataURL();
  img.className = 'share-card-preview';
  container.insertBefore(img, container.firstChild);

  // Download handler
  const downloadBtn = $('#share-download-btn');
  downloadBtn.onclick = () => {
    const a = document.createElement('a');
    a.href = canvas.toDataURL('image/png');
    a.download = 'my-shelter.png';
    a.click();
    showToast('이미지가 저장되었어요! 인스타그램에 올려주세요');
  };

  // Close handler
  const closeBtn = $('#share-close-btn');
  closeBtn.onclick = () => {
    overlay.classList.add('hidden');
  };
}

// ============================================================
// SHELTER VISIT (Feature #2)
// ============================================================
function encodeShelterState() {
  const data = {
    l: state.shelterLevel,
    p: state.placedItems.map(i => {
      const typeIndex = Object.keys(GACHA_ITEMS).indexOf(i.type);
      return [typeIndex, Math.round(i.x * 10) / 10, Math.round(i.y * 10) / 10];
    }),
    n: state.catNames,
  };
  if (typeof LZString === 'undefined') return null;
  return LZString.compressToEncodedURIComponent(JSON.stringify(data));
}

function decodeShelterState(encoded) {
  if (typeof LZString === 'undefined') return null;
  try {
    const json = LZString.decompressFromEncodedURIComponent(encoded);
    const data = JSON.parse(json);
    const itemKeys = Object.keys(GACHA_ITEMS);
    return {
      shelterLevel: data.l || 1,
      placedItems: (data.p || []).map((arr, idx) => ({
        id: idx + 1,
        type: itemKeys[arr[0]] || itemKeys[0],
        x: arr[1],
        y: arr[2],
      })),
      catNames: data.n || {},
    };
  } catch {
    return null;
  }
}

function shareShelterURL() {
  const encoded = encodeShelterState();
  if (!encoded) {
    showToast('공유 기능을 불러오는 중...');
    return;
  }

  const url = window.location.origin + window.location.pathname + '?shelter=' + encoded;
  navigator.clipboard.writeText(url).then(() => {
    showToast('쉼터 URL이 복사되었어요!');
  }).catch(() => {
    // Fallback
    const input = document.createElement('input');
    input.value = url;
    document.body.appendChild(input);
    input.select();
    document.execCommand('copy');
    input.remove();
    showToast('쉼터 URL이 복사되었어요!');
  });
}

function checkViewMode() {
  const params = new URLSearchParams(window.location.search);
  const shelterData = params.get('shelter');
  if (!shelterData) return false;

  const decoded = decodeShelterState(shelterData);
  if (!decoded) return false;

  enterViewMode(decoded);
  return true;
}

function enterViewMode(shelterData) {
  isViewMode = true;

  // Use temporary state
  state.shelterLevel = shelterData.shelterLevel;
  state.placedItems = shelterData.placedItems;
  state.catNames = shelterData.catNames;
  state.totalItemsPlaced = shelterData.placedItems.length;
  state.started = true;

  // Hide intro
  introOverlay.classList.add('hidden');

  // Hide sidebar
  const sidebar = $('#sidebar');
  sidebar.style.display = 'none';

  // Show view mode banner
  const banner = $('#view-mode-banner');
  banner.style.display = 'block';

  // Render
  updateFieldBackground();
  renderAllPlacedItems();
  syncCats();
  updateUI();
}

function exitViewMode() {
  window.location.href = window.location.origin + window.location.pathname;
}

// ============================================================
// SETTINGS PANEL (Feature #7)
// ============================================================
function toggleSettings() {
  const panel = $('#settings-panel');
  panel.classList.toggle('hidden');
}

function updateSpeedMultiplier(value) {
  state.catSpeedMultiplier = parseFloat(value);
  $('#speed-value').textContent = value + 'x';
  saveGame();
}

// ============================================================
// EVENT HANDLERS
// ============================================================
function setupEvents() {
  // Start button
  $('#start-btn').addEventListener('click', () => {
    state.started = true;
    introOverlay.classList.add('hidden');
    saveGame();
  });

  // Gacha button
  $('#gacha-btn').addEventListener('click', rollGacha);

  // Gacha modal close
  $('.gacha-overlay').addEventListener('click', closeGachaModal);
  $('#gacha-confirm-btn').addEventListener('click', closeGachaModal);

  // Field click for placement
  field.addEventListener('click', (e) => {
    if (isViewMode) return;
    if (!selectedInventoryItem) return;

    const rect = field.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    placeItem(selectedInventoryItem, x, y);
  });

  // Field mouse move for ghost
  field.addEventListener('mousemove', (e) => {
    if (!placementGhost) return;
    const rect = field.getBoundingClientRect();
    const x = e.clientX - rect.left - CONFIG.SPRITE_SIZE / 2;
    const y = e.clientY - rect.top - CONFIG.SPRITE_SIZE / 2;
    placementGhost.style.left = x + 'px';
    placementGhost.style.top = y + 'px';
  });

  // Right-click to cancel placement
  field.addEventListener('contextmenu', (e) => {
    if (selectedInventoryItem) {
      e.preventDefault();
      cancelPlacement();
    }
  });

  // ESC to cancel placement
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && selectedInventoryItem) {
      cancelPlacement();
    }
  });

  // Feature #7: Settings button
  const settingsBtn = $('#settings-btn');
  if (settingsBtn) {
    settingsBtn.addEventListener('click', toggleSettings);
  }

  // Feature #7: Speed slider
  const speedSlider = $('#speed-slider');
  if (speedSlider) {
    speedSlider.value = state.catSpeedMultiplier;
    $('#speed-value').textContent = state.catSpeedMultiplier + 'x';
    speedSlider.addEventListener('input', (e) => updateSpeedMultiplier(e.target.value));
  }

  // Feature #5: Name modal
  const nameConfirmBtn = $('#name-confirm-btn');
  if (nameConfirmBtn) {
    nameConfirmBtn.addEventListener('click', confirmNameModal);
  }
  const nameCancelBtn = $('#name-cancel-btn');
  if (nameCancelBtn) {
    nameCancelBtn.addEventListener('click', closeNameModal);
  }
  const nameOverlay = $('.name-modal-overlay');
  if (nameOverlay) {
    nameOverlay.addEventListener('click', closeNameModal);
  }
  // Enter key in name input
  const nameInput = $('#name-modal-input');
  if (nameInput) {
    nameInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') confirmNameModal();
    });
  }

  // Feature #1: Share button
  const shareBtn = $('#share-btn');
  if (shareBtn) {
    shareBtn.addEventListener('click', captureAndShare);
  }

  // Feature #2: Shelter share button
  const shelterShareBtn = $('#shelter-share-btn');
  if (shelterShareBtn) {
    shelterShareBtn.addEventListener('click', shareShelterURL);
  }

  // Feature #2: View mode buttons
  const exitViewBtn = $('#exit-view-btn');
  if (exitViewBtn) {
    exitViewBtn.addEventListener('click', exitViewMode);
  }
  const createOwnBtn = $('#create-own-btn');
  if (createOwnBtn) {
    createOwnBtn.addEventListener('click', exitViewMode);
  }

  // Close settings when clicking outside
  document.addEventListener('click', (e) => {
    const panel = $('#settings-panel');
    const btn = $('#settings-btn');
    if (panel && btn && !panel.contains(e.target) && !btn.contains(e.target)) {
      panel.classList.add('hidden');
    }
  });
}

// ============================================================
// GAME LOOP
// ============================================================
function gameLoop(timestamp) {
  if (!lastTime) lastTime = timestamp;
  const dt = Math.min(timestamp - lastTime, 100); // cap delta
  lastTime = timestamp;

  // Update cats
  for (const cat of cats) {
    cat.update(dt);
  }

  // Clean up old furballs
  if (!isViewMode) {
    updateFurballs();
  }

  // Auto-save
  if (!isViewMode) {
    saveTimer += dt;
    if (saveTimer >= CONFIG.SAVE_INTERVAL) {
      saveTimer = 0;
      saveGame();
    }
  }

  requestAnimationFrame(gameLoop);
}

// ============================================================
// INIT
// ============================================================
function init() {
  setupEvents();

  // Feature #2: Check if visiting someone's shelter
  if (checkViewMode()) {
    requestAnimationFrame(gameLoop);
    return;
  }

  const loaded = loadGame();

  if (loaded && state.started) {
    introOverlay.classList.add('hidden');
  }

  // Restore placed items
  renderAllPlacedItems();

  // Set correct background
  updateFieldBackground();

  // Spawn cats
  syncCats();

  // Update UI
  updateUI();

  // Check achievements on load (in case old save meets new criteria)
  checkAchievements();

  // Start game loop
  requestAnimationFrame(gameLoop);
}

init();
