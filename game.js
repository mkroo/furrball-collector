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
  // --- Common (16 new) ---
  newspaper:       { name: '신문지',       desc: '바스락바스락 최고의 장난감',       rarity: 'common', img: 'assets/gacha_items/newspaper.png' },
  paper_bag:       { name: '종이봉투',     desc: '들어가면 나오고 싶지 않아',       rarity: 'common', img: 'assets/gacha_items/paper_bag.png' },
  blanket:         { name: '담요',         desc: '따뜻한 낮잠의 필수품',            rarity: 'common', img: 'assets/gacha_items/blanket.png' },
  water_bowl:      { name: '물그릇',       desc: '시원한 물 한 그릇',               rarity: 'common', img: 'assets/gacha_items/water_bowl.png' },
  slipper:         { name: '슬리퍼',       desc: '왜 항상 한 짝만 사라질까',        rarity: 'common', img: 'assets/gacha_items/slipper.png' },
  tissue_box:      { name: '티슈박스',     desc: '뽑고 또 뽑고 끝이 없다',          rarity: 'common', img: 'assets/gacha_items/tissue_box.png' },
  sock:            { name: '양말',         desc: '발 냄새가 매력 포인트',            rarity: 'common', img: 'assets/gacha_items/sock.png' },
  shoe_box:        { name: '신발상자',     desc: '딱 맞는 사이즈의 집',             rarity: 'common', img: 'assets/gacha_items/shoe_box.png' },
  milk_carton:     { name: '우유팩',       desc: '빈 팩도 재미있어',                rarity: 'common', img: 'assets/gacha_items/milk_carton.png' },
  tin_can:         { name: '깡통',         desc: '데굴데굴 굴러가는 소리',          rarity: 'common', img: 'assets/gacha_items/tin_can.png' },
  leaf:            { name: '나뭇잎',       desc: '바람에 날리면 사냥 본능 발동',     rarity: 'common', img: 'assets/gacha_items/leaf.png' },
  pine_cone:       { name: '솔방울',       desc: '자연산 장난감',                   rarity: 'common', img: 'assets/gacha_items/pine_cone.png' },
  rubber_duck:     { name: '고무 오리',    desc: '삑삑! 오리인 척',                 rarity: 'common', img: 'assets/gacha_items/rubber_duck.png' },
  ball:            { name: '공',           desc: '단순하지만 영원한 재미',           rarity: 'common', img: 'assets/gacha_items/ball.png' },
  pencil:          { name: '연필',         desc: '굴러가는 게 제일 재미있어',        rarity: 'common', img: 'assets/gacha_items/pencil.png' },
  plastic_cup:     { name: '플라스틱 컵',  desc: '쓰러뜨리기 챌린지',               rarity: 'common', img: 'assets/gacha_items/plastic_cup.png' },
  // --- Rare (16 new) ---
  laser_pointer:   { name: '레이저 포인터', desc: '빨간 점의 유혹',                 rarity: 'rare',   img: 'assets/gacha_items/laser_pointer.png' },
  bell_toy:        { name: '방울 장난감',   desc: '딸랑딸랑 신나는 소리',            rarity: 'rare',   img: 'assets/gacha_items/bell_toy.png' },
  catnip:          { name: '캣닢',          desc: '한 번 맡으면 멈출 수 없어',       rarity: 'rare',   img: 'assets/gacha_items/catnip.png' },
  tunnel:          { name: '터널',          desc: '숨바꼭질 최고의 장소',            rarity: 'rare',   img: 'assets/gacha_items/tunnel.png' },
  hammock:         { name: '해먹',          desc: '흔들흔들 꿀잠 타임',              rarity: 'rare',   img: 'assets/gacha_items/hammock.png' },
  feather_wand:    { name: '깃털 낚시대',   desc: '점프 훈련 도구',                  rarity: 'rare',   img: 'assets/gacha_items/feather_wand.png' },
  mirror:          { name: '거울',          desc: '누구냥? 나냥!',                   rarity: 'rare',   img: 'assets/gacha_items/mirror.png' },
  music_box:       { name: '오르골',        desc: '잔잔한 자장가',                   rarity: 'rare',   img: 'assets/gacha_items/music_box.png' },
  ribbon:          { name: '리본',          desc: '화려한 꼬리 장식',                rarity: 'rare',   img: 'assets/gacha_items/ribbon.png' },
  brush:           { name: '빗',            desc: '빗질하면 골골골',                 rarity: 'rare',   img: 'assets/gacha_items/brush.png' },
  treat_jar:       { name: '간식통',        desc: '흔들면 달려오는 마법',             rarity: 'rare',   img: 'assets/gacha_items/treat_jar.png' },
  pillow:          { name: '베개',          desc: '머리 베기 딱 좋은 크기',           rarity: 'rare',   img: 'assets/gacha_items/pillow.png' },
  rug:             { name: '러그',          desc: '폭신한 발바닥 천국',              rarity: 'rare',   img: 'assets/gacha_items/rug.png' },
  basket:          { name: '바구니',        desc: '들어가면 딱 맞는 아늑함',          rarity: 'rare',   img: 'assets/gacha_items/basket.png' },
  lantern:         { name: '랜턴',          desc: '따뜻한 불빛 아래에서',             rarity: 'rare',   img: 'assets/gacha_items/lantern.png' },
  wind_chime:      { name: '풍경',          desc: '바람이 불면 딸랑',                rarity: 'rare',   img: 'assets/gacha_items/wind_chime.png' },
  // --- Epic (16 new) ---
  fountain:        { name: '분수대',        desc: '졸졸졸 흐르는 물소리',             rarity: 'epic',   img: 'assets/gacha_items/fountain.png' },
  tree_house:      { name: '나무집',        desc: '높은 곳을 좋아하는 고양이를 위해', rarity: 'epic',   img: 'assets/gacha_items/tree_house.png' },
  hot_spring:      { name: '온천',          desc: '포근한 김이 모락모락',             rarity: 'epic',   img: 'assets/gacha_items/hot_spring.png' },
  mini_castle:     { name: '미니 성',       desc: '고양이 왕국의 시작',              rarity: 'epic',   img: 'assets/gacha_items/mini_castle.png' },
  swing:           { name: '그네',          desc: '흔들흔들 하늘 위로',              rarity: 'epic',   img: 'assets/gacha_items/swing.png' },
  slide:           { name: '미끄럼틀',      desc: '슝~ 내려가는 재미',               rarity: 'epic',   img: 'assets/gacha_items/slide.png' },
  aquarium:        { name: '어항',          desc: '물고기 구경 최고의 자리',          rarity: 'epic',   img: 'assets/gacha_items/aquarium.png' },
  piano:           { name: '피아노',        desc: '밤마다 연주회 개최',              rarity: 'epic',   img: 'assets/gacha_items/piano.png' },
  tent:            { name: '텐트',          desc: '비밀 아지트 완성',                rarity: 'epic',   img: 'assets/gacha_items/tent.png' },
  fireplace:       { name: '벽난로',        desc: '따뜻한 불 옆 최고의 자리',        rarity: 'epic',   img: 'assets/gacha_items/fireplace.png' },
  chandelier:      { name: '샹들리에',      desc: '반짝반짝 럭셔리',                rarity: 'epic',   img: 'assets/gacha_items/chandelier.png' },
  telescope:       { name: '망원경',        desc: '새 관찰 전용',                   rarity: 'epic',   img: 'assets/gacha_items/telescope.png' },
  carousel:        { name: '회전목마',      desc: '빙글빙글 도는 꿈',               rarity: 'epic',   img: 'assets/gacha_items/carousel.png' },
  rainbow_arch:    { name: '무지개 아치',   desc: '쉼터의 상징',                    rarity: 'epic',   img: 'assets/gacha_items/rainbow_arch.png' },
  sakura_tree:     { name: '벚꽃나무',      desc: '꽃잎이 흩날리는 낭만',            rarity: 'epic',   img: 'assets/gacha_items/sakura_tree.png' },
  golden_bell:     { name: '황금 방울',     desc: '전설의 고양이 방울',              rarity: 'epic',   img: 'assets/gacha_items/golden_bell.png' },
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
let lastTime = 0;
let saveTimer = 0;
let dragState = null;
// { source: 'inventory'|'field', itemType, itemId, originItem?, originEl?,
//   ghostEl, startX, startY, dragging }

// ============================================================
// CAT CLASS
// ============================================================
class Cat {
  constructor(type) {
    this.type = type;
    this.el = document.createElement('img');
    this.el.className = 'cat-sprite';
    this.el.alt = CAT_NAMES[type] || type;

    const rect = field.getBoundingClientRect();
    this.x = Math.random() * (rect.width - CONFIG.SPRITE_SIZE);
    this.y = 100 + Math.random() * (rect.height - CONFIG.SPRITE_SIZE - 120);

    this.targetX = this.x;
    this.targetY = this.y;
    this.state = 'idle'; // idle | walking | sitting | sleeping | grooming
    this.stateTimer = this._randomIdle();
    this.dropTimer = this._randomDropTime();
    this.facingRight = true;

    // Animation state
    this.animState = 'idle';
    this.animFrame = 0;
    this.animTimer = 0;
    this.animSequence = ANIM_SEQUENCES.idle;
    this._updateSprite();

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

  // --- Animation methods ---
  _setAnimState(name) {
    if (this.animState === name) return;
    this.animState = name;
    this.animSequence = ANIM_SEQUENCES[name] || ANIM_SEQUENCES.idle;
    this.animFrame = 0;
    this.animTimer = this.animSequence.frameDuration;
    this._updateSprite();
  }

  _updateSprite() {
    const frameKey = this.animSequence.frames[this.animFrame];
    this.el.src = getCachedSprite(this.type, frameKey);
  }

  _advanceFrame(dt) {
    this.animTimer -= dt;
    if (this.animTimer <= 0) {
      this.animFrame = (this.animFrame + 1) % this.animSequence.frames.length;
      // Walk animation speed scales with cat speed
      let duration = this.animSequence.frameDuration;
      if (this.animState === 'walk') {
        duration = duration / (state.catSpeedMultiplier || 1.0);
      }
      this.animTimer = duration;
      this._updateSprite();
    }
  }

  update(dt) {
    // Advance frame animation
    this._advanceFrame(dt);

    this.stateTimer -= dt;

    // Furball drops (not while sleeping)
    if (!isViewMode && this.state !== 'sleeping') {
      this.dropTimer -= dt;
      if (this.dropTimer <= 0) {
        this._dropFurball();
        this.dropTimer = this._randomDropTime();
      }
    }

    const speedMult = state.catSpeedMultiplier || 1.0;

    if (this.state === 'idle') {
      this._setAnimState('idle');
      if (this.stateTimer <= 0) {
        // Transition: walking 50%, sitting 30%, grooming 20%
        const roll = Math.random();
        if (roll < 0.5) {
          this._pickTarget();
          this.state = 'walking';
          this._setAnimState('walk');
        } else if (roll < 0.8) {
          this.state = 'sitting';
          this.stateTimer = 3000 + Math.random() * 5000;
          this._setAnimState('sit');
        } else {
          this.state = 'grooming';
          this.stateTimer = 2000 + Math.random() * 2000;
          this._setAnimState('groom');
        }
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
        this._setAnimState('idle');
      } else {
        const speed = CONFIG.CAT_SPEED * speedMult * (dt / 16);
        this.x += (dx / dist) * speed * 2;
        this.y += (dy / dist) * speed * 2;
        this.facingRight = dx >= 0;
      }
    } else if (this.state === 'sitting') {
      if (this.stateTimer <= 0) {
        // Transition: sleeping 40%, idle 60%
        if (Math.random() < 0.4) {
          this.state = 'sleeping';
          this.stateTimer = 8000 + Math.random() * 12000;
          this._setAnimState('sleep');
        } else {
          this.state = 'idle';
          this.stateTimer = this._randomIdle();
          this._setAnimState('idle');
        }
      }
    } else if (this.state === 'sleeping') {
      if (this.stateTimer <= 0) {
        this.state = 'idle';
        this.stateTimer = this._randomIdle();
        this._setAnimState('idle');
      }
    } else if (this.state === 'grooming') {
      if (this.stateTimer <= 0) {
        this.state = 'idle';
        this.stateTimer = this._randomIdle();
        this._setAnimState('idle');
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
  el.src = `assets/furballs/${type}.svg`;
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
    slot.title = `${data.name} (${RARITY_LABELS[data.rarity]})`;

    const img = document.createElement('img');
    img.src = data.img;
    img.alt = data.name;
    img.draggable = false;
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

    slot.addEventListener('mousedown', (e) => {
      if (e.button !== 0) return;
      e.preventDefault();
      initDrag('inventory', itemId, null, null, null, e);
    });
    slot.addEventListener('touchstart', (e) => {
      initDrag('inventory', itemId, null, null, null, e);
    }, { passive: false });

    inv.appendChild(slot);
  }
}

// ============================================================
// DRAG AND DROP SYSTEM
// ============================================================
function initDrag(source, itemType, itemId, originItem, originEl, e) {
  if (isViewMode) return;
  const point = e.touches ? e.touches[0] : e;
  dragState = {
    source,
    itemType,
    itemId: itemId,
    originItem: originItem || null,
    originEl: originEl || null,
    ghostEl: null,
    startX: point.clientX,
    startY: point.clientY,
    dragging: false,
  };
}

function moveDrag(e) {
  if (!dragState) return;
  const point = e.touches ? e.touches[0] : e;

  if (!dragState.dragging) {
    const dx = point.clientX - dragState.startX;
    const dy = point.clientY - dragState.startY;
    if (Math.abs(dx) < 5 && Math.abs(dy) < 5) return;

    // Enter drag mode
    dragState.dragging = true;
    if (dragState.source === 'inventory') {
      $('#placement-hint').style.display = 'block';
    }

    // Create ghost element
    const data = GACHA_ITEMS[dragState.itemType];
    if (!data) { dragState = null; return; }

    const ghost = document.createElement('img');
    ghost.src = data.img;
    ghost.className = 'drag-ghost';
    ghost.style.position = 'fixed';
    ghost.style.width = CONFIG.SPRITE_SIZE + 'px';
    ghost.style.height = CONFIG.SPRITE_SIZE + 'px';
    ghost.style.pointerEvents = 'none';
    ghost.style.opacity = '0.8';
    ghost.style.zIndex = '1000';
    ghost.style.imageRendering = 'pixelated';
    ghost.style.left = (point.clientX - CONFIG.SPRITE_SIZE / 2) + 'px';
    ghost.style.top = (point.clientY - CONFIG.SPRITE_SIZE / 2) + 'px';
    document.body.appendChild(ghost);
    dragState.ghostEl = ghost;

    // If dragging from field, make original semi-transparent
    if (dragState.source === 'field' && dragState.originEl) {
      dragState.originEl.style.opacity = '0.3';
    }
  }

  // Update ghost position
  if (dragState.ghostEl) {
    dragState.ghostEl.style.left = (point.clientX - CONFIG.SPRITE_SIZE / 2) + 'px';
    dragState.ghostEl.style.top = (point.clientY - CONFIG.SPRITE_SIZE / 2) + 'px';
  }

  if (e.cancelable) e.preventDefault();
}

function endDrag(e) {
  if (!dragState) return;
  const ds = dragState;
  const point = e.changedTouches ? e.changedTouches[0] : e;

  if (!ds.dragging) {
    // Short click — not a drag
    if (ds.source === 'field' && ds.originItem && ds.originEl) {
      pickUpItem(ds.originItem, ds.originEl);
    }
    dragState = null;
    return;
  }

  // It was a drag — check drop target
  const dropX = point.clientX;
  const dropY = point.clientY;
  const fieldRect = field.getBoundingClientRect();
  const isInField = dropX >= fieldRect.left && dropX <= fieldRect.right &&
                    dropY >= fieldRect.top && dropY <= fieldRect.bottom;

  if (isInField) {
    const localX = dropX - fieldRect.left;
    const localY = dropY - fieldRect.top;

    if (ds.source === 'inventory') {
      // Place item from inventory onto field
      placeItem(ds.itemType, localX, localY);
    } else if (ds.source === 'field') {
      // Move placed item within field
      const xPercent = ((localX - CONFIG.SPRITE_SIZE / 2) / fieldRect.width) * 100;
      const yPercent = ((localY - CONFIG.SPRITE_SIZE / 2) / fieldRect.height) * 100;
      const xClamped = Math.max(0, Math.min(xPercent, 100 - (CONFIG.SPRITE_SIZE / fieldRect.width) * 100));
      const yClamped = Math.max(5, Math.min(yPercent, 100 - (CONFIG.SPRITE_SIZE / fieldRect.height) * 100));

      const placedItem = state.placedItems.find(i => i.id === ds.itemId);
      if (placedItem) {
        placedItem.x = xClamped;
        placedItem.y = yClamped;
      }
      if (ds.originEl) {
        ds.originEl.style.left = xClamped + '%';
        ds.originEl.style.top = yClamped + '%';
        ds.originEl.style.opacity = '1';
      }
      saveGame();
    }
  } else {
    // Dropped outside field — revert
    if (ds.source === 'field' && ds.originEl) {
      ds.originEl.style.opacity = '1';
    }
  }

  // Cleanup
  if (ds.ghostEl) ds.ghostEl.remove();
  $('#placement-hint').style.display = 'none';
  dragState = null;
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
  el.title = `${data.name} - 클릭: 회수 / 드래그: 이동`;
  el.dataset.itemId = item.id;
  el.draggable = false;

  el.addEventListener('mousedown', (e) => {
    if (e.button !== 0) return;
    if (isViewMode) return;
    e.stopPropagation();
    e.preventDefault();
    initDrag('field', item.type, item.id, item, el, e);
  });
  el.addEventListener('touchstart', (e) => {
    if (isViewMode) return;
    e.stopPropagation();
    initDrag('field', item.type, item.id, item, el, e);
  }, { passive: false });

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
    img.src = getCachedSprite(catType, 'idle_0');
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

  $('#name-modal-img').src = getCachedSprite(catType, 'idle_0');
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

  // Drag and drop — document-level handlers
  document.addEventListener('mousemove', moveDrag);
  document.addEventListener('touchmove', moveDrag, { passive: false });
  document.addEventListener('mouseup', endDrag);
  document.addEventListener('touchend', endDrag);

  // ESC to cancel drag
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && dragState) {
      if (dragState.source === 'field' && dragState.originEl) {
        dragState.originEl.style.opacity = '1';
      }
      if (dragState.ghostEl) dragState.ghostEl.remove();
      $('#placement-hint').style.display = 'none';
      dragState = null;
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
