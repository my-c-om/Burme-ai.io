// threeScene.js ကို ဒီလိုအဆင့်မြှင့်ပါ
import { EffectComposer, Bloom } from 'three/examples/jsm/postprocessing/EffectComposer.js';

// ရှိပြီးသား scene ကို ဖြည့်စွက်ခြင်း
const composer = new EffectComposer(renderer);
composer.addPass(new BloomPass(
  1.5,    // intensity
  25,     // kernel size
  0.4,    // sigma
  256     // blur scale
));

// ရေအောက်အလင်းရောင် effect
const waterGeometry = new THREE.PlaneGeometry(100, 100);
const waterMaterial = new THREE.MeshStandardMaterial({
  color: 0x44aaff,
  transparent: true,
  opacity: 0.8
});
const water = new THREE.Mesh(waterGeometry, waterMaterial);
water.rotation.x = -Math.PI / 2;
scene.add(water);
