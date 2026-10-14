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

export const siteConfig: SiteConfig = {
  brandName: "Quatra",
  tagline: "Software a medida para operaciones que no se detienen.",
  heroHeadline: "Tu operación no debe adaptarse al software. El software debe adaptarse a tu operación.",
  heroSubheadline: "Vamos a tu depósito o base logística, detectamos dónde se traban tus procesos y desarrollamos herramientas a medida para automatizar tareas repetitivas y recuperar cientos de horas-hombre al mes.",
  contactWhatsApp: "5491123456789", // Reemplazar con el número real de los hermanos
  contactEmail: "hola@quatra.io",
  location: "Buenos Aires, Argentina (Servicio presencial en planta y remoto)",
  navLinks: [
    { label: "El Problema", href: "#problema" },
    { label: "Los 4 Pilares", href: "#metodologia" },
    { label: "Calculadora de Horas", href: "#calculadora" },
    { label: "Soluciones", href: "#soluciones" },
    { label: "Nosotros", href: "#nosotros" },
    { label: "FAQ", href: "#faq" }
  ],
  pillars: [
    { number: "01", title: "Diagnóstico In-Situ", desc: "Vamos al muelle de carga y a las cabinas de despacho para ver el flujo real y cronometrar los cuellos de botella." },
    { number: "02", title: "Herramientas Satélite", desc: "Desarrollamos software y apps móviles que calzan en tu flujo sin obligarte a cambiar de sistema." },
    { number: "03", title: "Integración sin Fricción", desc: "Conectamos tus Excels, ERPs existentes, facturación y WhatsApp para eliminar la carga duplicada." },
    { number: "04", title: "Medición de Horas-Hombre", desc: "Acompañamos a tu personal en el piso y garantizamos el ahorro medible de tiempo desde la semana 1." }
  ]
};

// Helper for GitHub Pages subpath compatibility
export function asset(p: string): string {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  const clean = p.startsWith('/') ? p : `/${p}`;
  return `${base}${clean}`;
}
