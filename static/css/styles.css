* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background: #111;
    font-family: 'Segoe UI', sans-serif;
}

.sidebar {
    width: 55px;
    height: 100vh;
    background-color: #0f0f0f;
    color: white;
    padding: 1rem 0;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: width 0.3s ease;
    overflow: hidden;
}

.sidebar:hover {
    width: 180px;
}

.logo {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 0 1rem;
    margin-bottom: 2rem;
}

.logo img {
    width: 170px;
    height: 35px;
}

.logo-text {
    display: none;
}

.sidebar:hover .logo-text {
    display: inline;
}

.menu .menu-option {
    color: #ffffff;
    text-decoration: none;
}

.bottom-menu a {
    color: #ffffff;
    text-decoration: none;
}

.menu,
.bottom-menu {
    list-style: none;
}

.menu li,
.bottom-menu li {
    display: flex;
    align-items: center;
    padding: 1rem;
    gap: 1rem;
    position: relative;
    cursor: pointer;
    transition: background 0.2s;
}

.menu li:hover,
.bottom-menu li:hover {
    background: #1a1a1a;
}

.icon {
    font-size: 1.2rem;
}

.menu li a span,
.bottom-menu li span {
    display: none;
}

.sidebar:hover li a {
    display: flex;
}

.sidebar:hover li a span {
    display: inline;
    padding-left: 12px;
}

.badge {
    position: absolute;
    right: 1rem;
    background: #a48fff;
    color: black;
    font-size: 0.75rem;
    padding: 2px 6px;
    border-radius: 12px;
    display: none;
}

.sidebar:hover .has-badge .badge {
    display: inline;
}

.content {
    padding: 2rem;
}

.content a {
    text-decoration: none;
    color: #1a1a1a;
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
}

.card {
    background-color: white;
    border-radius: 10px;
    padding: 1.5rem;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
}

.card h3 {
    margin-bottom: 1rem;
    font-size: 1.1rem;
}

.card p {
    font-size: 1.5rem;
    font-weight: bold;
}

/* Estructura de layout principal */
.layout {
    display: flex;
    height: 100vh;
}

/* Sidebar ya existente (sin cambios mayores) */

/* Contenedor del contenido principal */
.main-content {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    background-color: #f0f0f0;
    transition: margin-left 0.3s ease;
}

/* Header como parte del contenido principal */
.header {
    height: 60px;
    background: #fdfdfd;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 2rem;
    border-bottom: 1px solid #eee;
}

/* Estilos del buscador */
.search-box {
    display: flex;
    align-items: center;
    background: white;
    padding: 0.5rem 1rem;
    border-radius: 10px;
    border: 1px solid #ddd;
    width: 300px;
}

.search-box .icon {
    margin-right: 8px;
    color: #666;
}

.search-box input {
    border: none;
    outline: none;
    background: transparent;
    width: 100%;
    font-size: 1rem;
}

/* Iconos a la derecha del header */
.header-right {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.icon-button {
    background: #fff;
    padding: 8px;
    border-radius: 50%;
    box-shadow: 0 0 4px rgba(0, 0, 0, 0.1);
    cursor: pointer;
}

.avatar img {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    object-fit: cover;
}

/* Main (contenido debajo del header) */
main {
    flex-grow: 1;
    padding: 2rem;
    background-color: #fdfdfd;
}

/*Couse*/

.course-card img {
    width: 100%;
    height: 200px;
}

.author {
    display: flex;
    align-items: center;
}

.author img {
    width: 40px;
    height: auto;
    border-radius: 50%;
    border: 2px solid #1d1438;
    background: white;
}

.author span {
    padding-left: 10px;
    color: #666;
}

i.fa-solid.fa-star {
    color: #ccaa2f;
}

/* === RESPONSIVE CAROUSEL WRAPPER === */
.carousel-wrapper {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    scroll-snap-type: x mandatory;
    padding-left: 1rem;
}

.course-rating {
    display: flex;
    justify-content: space-between;
    padding: 5px 0px;
}

.course-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    padding: 2rem;
}

.course-card a {
    text-decoration: none;
    color: #0f0f0f;
}

.course-title {
    text-decoration: none;
    padding: 5px 0px;
}

/* Mobile: convierte en carrusel horizontal */
@media (max-width: 768px) {
    .course-grid {
        display: flex;
        gap: 1rem;
        padding: 1rem 0;
        min-width: 100%;
    }

    .course-card {
        flex: 0 0 auto;
        scroll-snap-align: start;
        width: 280px;
    }
}


/* === CURSO DETALLE LAYOUT === */
.course-layout {
    display: flex;
    gap: 2rem;
    padding: 2rem;
    flex-wrap: wrap;
    background: #f0f0f0;
    color: #0f0f0f;
}

/* Secciones izquierda */
.course-sections {
    flex: 1 1 500px;
}

.course-sections h2 {
    font-size: 1.8rem;
    margin-bottom: 1.5rem;
}

/* Accordion */
.accordion-item {
    border-bottom: 1px solid #333;
}

.accordion-header {
    background: none;
    border: none;
    color: #0f0f0f;
    font-size: 1rem;
    padding: 1rem 0;
    width: 100%;
    text-align: left;
    cursor: pointer;
    font-weight: 500;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.accordion-header::after {
    content: "⌄";
    font-size: 0.9rem;
    transform: rotate(0deg);
    transition: transform 0.3s;
}

/* Card derecha */
.course-info-card {
    flex: 1 1 320px;
    background: #fefefe;
    border-radius: 12px;
    /* overflow: hidden; */
    /* box-shadow: 0 0 20px rgba(0, 0, 0, 0.1); */
}

.card-banner {
    position: relative;
}

.card-banner .tag {
    position: absolute;
    top: 10px;
    left: 10px;
    background: #ffffff;
    color: #000;
    font-size: 0.75rem;
    padding: 4px 10px;
    border-radius: 20px;
}

.card-banner img:first-of-type {
    width: 100%;
    height: 180px;
    object-fit: contain;
    background: #0f0f0f;
}

.author-avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    position: absolute;
    bottom: -24px;
    right: 16px;
    border: 2px solid #1d1438;
    background: white;
}

.card-body {
    padding: 2.5rem 1.5rem 1.5rem;
    margin-bottom: 40px;

}

.card-body h3 {
    margin-bottom: 1rem;
    font-size: 1.2rem;
}

.course-details {
    list-style: none;
    padding: 0;
}

.course-details li {
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.95rem;
}

.accordion-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
    padding-left: 1rem;
}

.accordion-content ul {
    list-style: disc;
    margin: 0.5rem 0 1rem;
    padding-left: 1rem;
    color: #1d1438;
    font-size: 0.95rem;
}

.accordion-content ul li {
    list-style: none;
    padding: 8px 0px;
}

.accordion-content ul li i.fa-solid {
    padding: 0px 10px 0px 0px;
}

a.btn {
    text-decoration: none;
    color: #ffffff;
    background-color: #1d1438;
    padding: 15px 20px;
    /* margin-top: 20px; */
    display: block;
    height: auto;
    width: 100%;
    border-radius: 10px;
    text-align: center;
    font-size: 16px;
}

/* .accordion-content ul li:before {
    content: '✓';
} */

.accordion-item.active .accordion-content {
    max-height: 300px;
    /* ajusta según el contenido */
}

.accordion-item.active .accordion-header::after {
    transform: rotate(180deg);
}


/* === Responsive Sidebar Toggle === */
.menu-toggle {
    display: none;
    background: none;
    border: none;
    font-size: 1.8rem;
    color: #333;
    cursor: pointer;
}

/*Profile*/
.profile-container {
    padding: 2rem;
    border-radius: 10px;
    width: 100%;
    max-width: 800px;
    display: flex;
    gap: 2rem;
    flex-wrap: wrap;
}

.profile-picture {
    flex: 1 1 200px;
    text-align: center;
}

.profile-picture img {
    width: 140px;
    height: 140px;
    object-fit: cover;
    border-radius: 50%;
    border: 2px solid #1e1e1e;
}

.profile-picture label {
    display: block;
    margin-top: 1rem;
    font-size: 0.9rem;
    color: #1e1e1e;
    cursor: pointer;
}

.profile-form {
    flex: 2 1 400px;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.profile-form h2 {
    margin-bottom: 1rem;
}

.input-group {
    display: flex;
    flex-direction: column;
}

.input-group label {
    font-size: 0.85rem;
    margin-bottom: 0.4rem;
    color: #1e1e1e;
}

.input-group input,
.input-group select {
    border: 1px solid #555;
    padding: 0.6rem;
    border-radius: 5px;
    color: #1e1e1e;
}

.input-row {
    display: flex;
    gap: 1rem;
}

.input-row .input-group {
    flex: 1;
}

.submit-btn {
    background-color: #1e1e1e;
    border: none;
    padding: 0.8rem 1.2rem;
    border-radius: 6px;
    color: #ffffff;
    font-weight: bold;
    cursor: pointer;
    align-self: flex-start;
}

.submit-btn:hover {
    background-color: #666;
}

@media (max-width: 768px) {
    .layout {
        flex-direction: column;
    }

    .menu-toggle {
        display: block;
    }

    .sidebar {
        position: fixed;
        top: 60px;
        /* altura del header */
        left: -100%;
        width: 220px;
        height: calc(100%);
        background: #0f0f0f;
        z-index: 1000;
        transition: left 0.3s ease;
    }

    .menu li a span,
    .bottom-menu li span,
    .bottom-menu li a {
        display: flex;
        gap: 10px;
    }

    .menu .menu-option {
        display: flex;
        gap: 10px;
    }



    .sidebar.open {
        left: 0;
        top: 0;
    }

    .main-content {
        padding: 1rem;
    }

    /* Carrusel de cursos */
    .course-grid {
        display: flex;
        overflow-x: auto;
        gap: 1rem;
        scroll-snap-type: x mandatory;
        flex-flow: wrap;
    }

    .course-card {
        flex: 0 0 auto;
        width: 280px;
        scroll-snap-align: start;
    }
}