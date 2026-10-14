export interface SiteConfig {
  brandName: string;
  tagline: string;
  heroHeadline: string;
  heroSubheadline: string;
  contactWhatsApp: string;
  contactEmail: string;
  location: string;
  navLinks: { label: string; href: string }[];
  pillars: { number: string; title: string; desc: string }[];
}

// Robust URL helper ensuring correct trailing base URL
export const baseUrl = import.meta.env.BASE_URL.endsWith('/') 
  ? import.meta.env.BASE_URL 
  : `${import.meta.env.BASE_URL}/`;

export function url(path: string = ''): string {
  const clean = path.replace(/^\//, '');
  return `${baseUrl}${clean}`;
}

export const siteConfig: SiteConfig = {
  brandName: "Quatra",
  tagline: "Consultoría de rendimiento y optimización de procesos para logística PyME.",
  heroHeadline: "Mejoramos el rendimiento de tu logística. En el terreno y a la medida de tu equipo.",
  heroSubheadline: "No somos una empresa de software ni vendemos licencias enlatadas. Somos consultores operativos: vamos a tu depósito, auditamos el flujo real de trabajo y creamos herramientas y programas especializados para que tu equipo recupere cientos de horas-hombre al mes.",
  contactWhatsApp: "5491123456789", // Reemplazar con el número real de los hermanos
  contactEmail: "contacto@quatra.io",
  location: "Buenos Aires, Argentina (Servicio presencial en planta y remoto)",
  navLinks: [
    { label: "Enfoque", href: "#enfoque" },
    { label: "Los 4 Pilares", href: "#pilares" },
    { label: "Calculadora de Horas", href: "#calculadora" },
    { label: "Soluciones", href: "#soluciones" },
    { label: "Nosotros", href: "#nosotros" },
    { label: "Logo & Brand Kit", href: url("logo") }
  ],
  pillars: [
    { number: "01", title: "Auditoría Operativa In-Situ", desc: "Vamos a tu muelle de carga y depósito. Observamos cómo trabaja tu personal, medimos cuellos de botella y cronometramos pérdidas de tiempo." },
    { number: "02", title: "Rediseño de Flujo de Trabajo", desc: "Simplificamos tareas, eliminamos pasos innecesarios y erradicamos la duplicación de datos entre sectores." },
    { number: "03", title: "Programas y Tools a Medida", desc: "Cuando hace falta tecnología, desarrollamos programas específicos que se adaptan a tus procesos y no tu equipo al software." },
    { number: "04", title: "Medición de Rendimiento", desc: "Capacitamos en planta y auditamos las horas-hombre recuperadas y la aceleración de tus despachos desde la primera semana." }
  ]
};
