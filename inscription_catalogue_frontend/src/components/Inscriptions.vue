<template>
    <div class="inscription_container">
        <div class="inscription_content">
            <p class="inscription_list_results">{{ inscriptions.length }} resultados encontrados.</p>
            <ul class="inscription_list">
                <li v-for="inscription in inscriptions" :key="inscription.id">
                    <div class="inscription_images_container"></div>
                    <div class="inscription_description">
                        <p><strong>Referencia Hesperia</strong>:&nbsp;{{ inscription.refHesperia }}</p>
                        <p><strong>Texto</strong>:&nbsp;{{ inscription.text }}</p>
                        <p><strong>Yacimiento</strong>:&nbsp;{{ inscription.site }}</p>
                        <p><strong>Referencia HMLH</strong>:&nbsp;{{ inscription.refMLH }}</p>
                        <p><strong>Municipio</strong>:&nbsp;{{ inscription.town }}</p>
                        <p><strong>Provincia</strong>:&nbsp;{{ inscription.province }}</p>
                        <p><strong>Material</strong>:&nbsp;{{ inscription.material }}</p>
                        <p><strong>Soporte</strong>:&nbsp;{{ inscription.medium }}</p>
                        <p><strong>Signario</strong>:&nbsp;{{ inscription.writing_script }}</p>
                        <p><strong>Dirección de escritura</strong>:&nbsp;{{ inscription.writing_direction }}</p>
                        <p><strong>Sistema dual</strong>:&nbsp;{{ inscription.dual_system }}</p>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                inscriptions: ['']
            }
        },
        methods: {
            async getData() {
                try {
                    const response = await fetch('http://localhost:8000/api/inscriptions/');
                    this.inscriptions = await response.json();
                } catch (error) {
                    console.log(error);
                }
            },
        },
        created() {
            this.getData();
        }
    }
</script>