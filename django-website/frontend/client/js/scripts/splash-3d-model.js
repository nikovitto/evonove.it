// Global variables
let renderer;
let scene;
let camera;

let controls;

const fov = 35;

const start = Date.now();

const splashCanvas = document.querySelector('.splash-3dmodels');

let mobile;

if (window.innerWidth <= 980) {
  mobile = true;
}

/**
 * Function handles the resize event. This make sure the camera and the
 * renderer are updated at the correct moment.
 */
function onWindowResize() {
  renderer.setSize(window.innerWidth, window.innerHeight);
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
}

/**
 * Set a delay time before onWindowResize() runs. This delay allows time to
 * Android devices for recalculate the viewport sizes before the orientation
 * change event is triggered.
 */
function onOrientationChange() {
  setTimeout(onWindowResize, 1000);
}

/**
 * Render the scene and delegate to requestAnimationFrame for future renders.
 */
function render() {
  renderer.render(scene, camera);
  requestAnimationFrame(render);
}

/**
 * Render the scene of 3D model.
 */
function renderSplashModel() {
  // Create a scene
  scene = new THREE.Scene();

  // Create a camera and place it 100 units away, looking towards the center of the scene.
  camera = new THREE.PerspectiveCamera(fov, window.innerWidth / window.innerHeight, 1, 10000);
  camera.position.z = 100;

  // Create a shader material
  const material = new THREE.ShaderMaterial({
    vertexShader: document.getElementById('vertexShader').textContent,
    fragmentShader: document.getElementById('fragmentShader').textContent,
    wireframe: true,
  });

  // Create a sphere and assign the material
  const mesh = new THREE.Mesh(new THREE.IcosahedronGeometry(20, 4), material);
  scene.add(mesh);

  // Create the renderer and attach it to the DOM
  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setClearColor(0x242528, 1.0);
  renderer.setPixelRatio(window.devicePixelRatio);

  // Add the output of the renderer to the html element
  splashCanvas.appendChild(renderer.domElement);

  if (!mobile) {
    // Controls shall be granted for large screens only.
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableZoom = false;

    // Recalculate the scene's sizes on window resize events.
    // Resize events are triggered on large screens only.
    onWindowResize();
    window.addEventListener('resize', onWindowResize);
  } else {
    // Detect orientation change event on mobile devices in order to recalculate
    // the scene's sizes.
    window.addEventListener('orientationchange', onOrientationChange);
  }

  render();
}

// Render the 3D model after the page is load.
window.addEventListener('load', renderSplashModel);
