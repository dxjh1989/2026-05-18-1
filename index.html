<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML5 Minecraft Clone</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            background-color: #78a7ff; /* 麥塊藍天色 */
            font-family: sans-serif;
            user-select: none;
        }
        #ui {
            position: absolute;
            top: 20px;
            left: 20px;
            color: white;
            text-shadow: 2px 2px 0px #000;
            font-size: 16px;
            pointer-events: none;
            line-height: 1.5;
        }
        /* 畫面中央的經典十字準心 */
        #crosshair {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 20px;
            height: 20px;
            transform: translate(-50%, -50%);
            pointer-events: none;
        }
        #crosshair::before, #crosshair::after {
            content: '';
            position: absolute;
            background: white;
            mix-blend-mode: difference; /* 讓準心在不同顏色背景都看得見 */
        }
        #crosshair::before { top: 9px; left: 0; width: 20px; height: 2px; }
        #crosshair::after { top: 0; left: 9px; width: 2px; height: 20px; }

        #instructions {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            background: rgba(0,0,0,0.75);
            padding: 30px;
            border: 4px solid #333;
            border-radius: 4px;
            text-align: center;
            cursor: pointer;
        }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/PointerLockControls.js"></script>
</head>
<body>

    <div id="ui">
        <div>OnerWorld 測試版</div>
        <div>位置: X: <span id="posX">0</span>, Y: <span id="posY">0</span>, Z: <span id="posZ">0</span></div>
    </div>
    <div id="crosshair"></div>
    <div id="instructions">
        <h2 style="color: #55ff55;">MINECRAFT HTML5</h2>
        <p>點擊畫面 開始建造/破壞</p>
        <p style="font-size: 14px; color: #aaa;">
            移動：W, A, S, D<br>
            跳躍：Space 空白鍵<br>
            <span style="color: #ff5555;">破壞方塊：滑鼠左鍵</span><br>
            <span style="color: #55ffff;">放置方塊：滑鼠右鍵</span>
        </p>
    </div>

    <script>
        // --- 1. 場景與渲染設定 ---
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x78a7ff);
        scene.fog = new THREE.FogExp2(0x78a7ff, 0.02);

        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: false }); // 關閉反鋸齒，更有像素感
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.shadowMap.enabled = true;
        document.body.appendChild(renderer.domElement);

        // --- 2. 光線 (Minecraft 風格的強烈陽光) ---
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
        scene.add(ambientLight);

        const dirLight = new THREE.DirectionalLight(0xffffff, 0.6);
        dirLight.position.set(40, 100, 20);
        dirLight.castShadow = true;
        scene.add(dirLight);

        // --- 3. 方塊材質與設定 ---
        const BLOCK_SIZE = 2; // 每個方塊的大小
        const worldBlocks = []; // 儲存所有方塊的陣列，用來做碰撞與滑鼠點擊偵測

        // 簡單做出草地與泥土的顏色區分
        const grassMaterial = new THREE.MeshStandardMaterial({ color: 0x5b8731, roughness: 0.9 });
        const dirtMaterial = new THREE.MeshStandardMaterial({ color: 0x866043, roughness: 0.9 });
        const blockGeometry = new THREE.BoxGeometry(BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);

        // --- 4. 生成世界 (16x16 的區塊，共兩層：表面草地，下層泥土) ---
        const WORLD_SIZE = 16;
        function generateWorld() {
            for (let x = -WORLD_SIZE; x < WORLD_SIZE; x++) {
                for (let z = -WORLD_SIZE; z < WORLD_SIZE; z++) {
                    // 第一層：草地 (Y = 0)
                    createBlock(x * BLOCK_SIZE, 0, z * BLOCK_SIZE, grassMaterial);
                    // 第二層：泥土 (Y = -2)
                    createBlock(x * BLOCK_SIZE, -BLOCK_SIZE, z * BLOCK_SIZE, dirtMaterial);
                }
            }
        }

        function createBlock(x, y, z, material) {
            const block = new THREE.Mesh(blockGeometry, material);
            block.position.set(x, y, z);
            block.castShadow = true;
            block.receiveShadow = true;
            scene.add(block);
            worldBlocks.push(block);
        }

        generateWorld();

        // --- 5. 玩家與控制 ---
        const controls = new THREE.PointerLockControls(camera, document.body);
        const instructions = document.getElementById('instructions');

        instructions.addEventListener('click', () => controls.lock());
        controls.addEventListener('lock', () => instructions.style.display = 'none');
        controls.addEventListener('unlock', () => instructions.style.display = 'block');
        scene.add(controls.getObject());

        // 玩家初始位置 (站在草地上方)
        controls.getObject().position.set(0, 4, 0);

        // --- 6. 鍵盤與滑鼠操控 ---
        const move = { forward: false, backward: false, left: false, right: false };
        let velocity = new THREE.Vector3();
        let direction = new THREE.Vector3();
        let canJump = false;

        document.addEventListener('keydown', (e) => {
            switch (e.code) {
                case 'KeyW': move.forward = true; break;
                case 'KeyS': move.backward = true; break;
                case 'KeyA': move.left = true; break;
                case 'KeyD': move.right = true; break;
                case 'Space': if (canJump) velocity.y += 12; canJump = false; break;
            }
        });

        document.addEventListener('keyup', (e) => {
            switch (e.code) {
                case 'KeyW': move.forward = false; break;
                case 'KeyS': move.backward = false; break;
                case 'KeyA': move.left = false; break;
                case 'KeyD': move.right = false; break;
            }
        });

        // --- 7. 核心：破壞與放置方塊 (Raycaster 視線操作) ---
        const raycaster = new THREE.Raycaster();
        const mouse = new THREE.Vector2(0, 0); // 瞄準畫面正中央

        document.addEventListener('mousedown', (e) => {
            if (!controls.isLocked) return;

            // 從相機中心發射一條視線
            raycaster.setFromCamera(mouse, camera);
            // 設定最遠只能挖到 15 單位距離的方塊
            raycaster.far = 15; 
            const intersects = raycaster.intersectObjects(worldBlocks);

            if (intersects.length > 0) {
                const intersect = intersects[0];

                if (e.button === 0) {
                    // 【左鍵：破壞方塊】
                    scene.remove(intersect.object);
                    const index = worldBlocks.indexOf(intersect.object);
                    if (index > -1) worldBlocks.splice(index, 1);
                } 
                else if (e.button === 2) {
                    // 【右鍵：放置方塊】
                    // intersect.face.normal 會告訴我們滑鼠點到的是方塊的哪一面(上、下、左、右、前、後)
                    const normal = intersect.face.normal;
                    const newPosition = intersect.object.position.clone().add(
                        normal.clone().multiplyScalar(BLOCK_SIZE)
                    );

                    // 在新位置蓋一個草地方塊
                    createBlock(newPosition.x, newPosition.y, newPosition.z, grassMaterial);
                }
            }
        });

        // 阻擋瀏覽器右鍵選單，避免干擾放方塊
        document.addEventListener('contextmenu', e => e.preventDefault());

        // --- 8. 遊戲主迴圈 (物理與渲染) ---
        const clock = new THREE.Clock();
        const uiX = document.getElementById('posX');
        const uiY = document.getElementById('posY');
        const uiZ = document.getElementById('posZ');

        function animate() {
            requestAnimationFrame(animate);

            if (controls.isLocked) {
                const delta = clock.getDelta();

                // 模擬物理阻力
                velocity.x -= velocity.x * 10.0 * delta;
                velocity.z -= velocity.z * 10.0 * delta;
                velocity.y -= 9.8 * 3.5 * delta; // 重力

                direction.z = Number(move.forward) - Number(move.backward);
                direction.x = Number(move.right) - Number(move.left);
                direction.normalize();

                if (move.forward || move.backward) velocity.z -= direction.z * 120.0 * delta;
                if (move.left || move.right) velocity.x -= direction.x * 120.0 * delta;

                controls.moveRight(-velocity.x * delta);
                controls.moveForward(-velocity.z * delta);
                controls.getObject().position.y += (velocity.y * delta);

                // 簡易地板碰撞 (防止掉進虛空)
                if (controls.getObject().position.y < 3) {
                    velocity.y = 0;
                    controls.getObject().position.y = 3;
                    canJump = true;
                }

                // 更新座標 UI (轉換成 Minecraft 的方塊座標單位)
                uiX.innerText = Math.floor(controls.getObject().position.x / BLOCK_SIZE);
                uiY.innerText = Math.floor(controls.getObject().position.y / BLOCK_SIZE) - 1;
                uiZ.innerText = Math.floor(controls.getObject().position.z / BLOCK_SIZE);
            }

            renderer.render(scene, camera);
        }

        animate();

        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
    </script>
</body>
</html>
