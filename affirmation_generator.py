import random
import json

class AffirmationGenerator:
    def __init__(self):
        self.categories = {
            "Self-Love": [
                "I am enough, just as I am.",
                "I am worthy of love, joy, and respect in every way.",
                "I am proud of the person I am becoming, growing stronger each day.",
                "I accept myself fully, with compassion and grace.",
                "I radiate beauty from within and cherish who I am.",
                "With kindness and respect, I honor myself deeply.",
                "I celebrate my unique strengths and embrace my individuality.",
                "I am open to all the goodness life has to offer, knowing I am worthy.",
                "I trust in myself and the path I choose to walk."
                "My boundaries are sacred; I honor them with courage and strength.",
                "I am falling in love with the person I am becoming.",
                "I am grateful for who I am today and the journey that brought me here.",
                "I release the weight of past mistakes and choose to move forward with love.",
                "I believe in my abilities and in the power within me.",
                "I am deserving of love, kindness, and compassion in all its forms.",
                "I am a priority in my life, and I honor my needs.",
                "I let go of self-doubt and step boldly into confidence.",
                "I love myself enough to walk away from anything that doesn't serve me.",
                "I am worthy of a life filled with joy and fulfillment.",
                "I embrace every part of myself, loving even the imperfections.",
                "I am deserving of a peaceful, happy life.",
                "I am the author of my happiness and self-worth.",
                "I am grateful for my body and all it allows me to experience.",
                "I trust the beautiful process of becoming my best self.",
                "I celebrate every victory, no matter how small, as a step forward.",
                "I am proud of my resilience and the strength that has brought me here.",
                "My past does not define me; I am the creator of my future.",
                "I am enough, and I give my best every day.",
                "I shine with confidence and self-respect.",
                "I treat myself with gentleness, knowing I am doing my best.",
                "I am worthy of love and belonging, just as I am.",
                "I cherish the gift of being myself.",
                "Every day, I learn to love myself more deeply.",
                "My uniqueness is my strength, and I embrace it fully.",
                "I respect myself and listen to my inner needs.",
                "I am a beautiful work in progress, proud of my journey.",
                "I deserve to feel wonderful about who I am.",
                "I am my own best friend, always standing by myself.",
                "My imperfections are part of my beauty; they make me who I am.",
                "I love myself enough to put my needs first.",
                "I am grateful for the harmony of my mind, body, and spirit.",
                "I trust myself to make wise, fulfilling choices.",
                "I am patient with my growth and allow space for transformation.",
                "I hold confidence in my abilities and in my worth.",
                "I welcome all the goodness coming my way, knowing I am deserving.",
                "I am a soul of light and love, deserving of respect.",
                "I am whole, complete, and perfect in this moment.",
                "Today and every day, I love myself unconditionally.",
                "I alone determine my worth, and I will never settle for less than I deserve.",
                "The way I love myself teaches others how to love me."
            ],
            "Relationship": [
                "True love flows naturally; the right person will choose me each day without question.",
                "A healthy relationship is built on respect, trust, and understanding. I will seek a partner who inspires growth and uplifts my spirit.",
                "I am worthy of a love that honors my heart, mind, and spirit.",
                "I attract people who bring joy, support, and encouragement into my life.",
                "Healthy boundaries are a form of self-respect, and I embrace them in every connection.",
                "I choose relationships that uplift my spirit and enrich my soul.",
                "I open my heart to give and receive love in balanced, meaningful ways.",
                "The right person will love me as I am, with all my uniqueness.",
                "I deserve relationships that make me feel safe, cherished, and valued.",
                "I welcome genuine connections that bring growth, peace, and happiness.",
                "I am worthy of deep, unconditional love and affection.",
                "I am grateful for the loving and supportive people in my life.",
                "I trust that the right connections will appear in my life at the perfect time.",
                "I let go of control and allow my relationships to unfold naturally and harmoniously.",
                "I am open to relationships that resonate with my values and highest vision.",
                "I deserve a partner who values, respects, and cherishes me deeply.",
                "I surround myself with people who encourage my growth and happiness.",
                "I am capable of creating connections that are meaningful and lasting.",
                "I attract people who honor my boundaries and embrace my individuality.",
                "I am worthy of love that is honest, uplifting, and supportive.",
                "The love I seek seeks me as well, and I am open to its arrival.",
                "I trust the universe to bring compassionate and loving souls into my life.",
                "I release any relationships that no longer nurture my growth and well-being.",
                "I am a loving presence, attracting relationships that are fulfilling and genuine.",
                "I am grateful for the respect, love, and joy in my relationships.",
                "I nurture relationships that allow me to be true to myself.",
                "I am worthy of relationships that bring joy, peace, and growth.",
                "I attract partners who encourage my dreams and support my journey.",
                "I am open to love that is both healing and empowering.",
                "My relationships reflect my values and bring out my highest self.",
                "I am deserving of a love that feels secure, joyful, and deeply fulfilling.",
                "I release past hurts and open myself to beautiful new connections.",
                "I choose love, peace, and joy in all my relationships.",
                "I attract people who honor my dreams, needs, and individuality.",
                "I deserve a relationship that feels safe, nurturing, and uplifting.",
                "I am thankful for relationships that fill my heart with happiness and serenity.",
                "I create space for those who embrace me just as I am.",
                "I am ready for a relationship that elevates my spirit.",
                "I am worthy of a partnership grounded in trust and mutual respect.",
                "I choose relationships that empower and value me.",
                "I am deserving of love that uplifts and supports my journey.",
                "I attract kind, genuine, and compassionate people into my life.",
                "I welcome relationships that enrich my life with love and positivity.",
                "I am open to a love that is genuine, honest, and fulfilling.",
                "I welcome harmony and happiness into my life through meaningful connections.",
                "I am worthy of a partner who appreciates my true self.",
                "I release all fears and welcome a love that’s real and true.",
                "I attract relationships that align with my soul’s highest purpose.",
                "I deserve relationships filled with joy, laughter, and unconditional love.",
                "I am grateful for relationships that nurture my soul and support my growth."
            ],
            "Motivation": [
                "I am capable of achieving extraordinary things.",
                "Every day, I move closer to my dreams with confidence.",
                "I am unstoppable; challenges only strengthen my resolve.",
                "I trust fully in my ability to succeed.",
                "I am determined to make today both productive and meaningful.",
                "My purpose and passion fuel my journey to success.",
                "I am focused and persistent, moving forward with unstoppable energy.",
                "I transform my dreams into clear, achievable goals.",
                "I am stronger than any obstacle that comes my way.",
                "I hold the power to create meaningful change in my life.",
                "I am fully committed to my growth and success.",
                "I celebrate my accomplishments and look forward to the future with excitement.",
                "I am energized and motivated to reach my fullest potential.",
                "I choose to rise above every limiting belief that tries to hold me back.",
                "I am dedicated, and my hard work is already showing results.",
                "I am resilient and face challenges with strength and courage.",
                "I am motivated to give my best in every moment.",
                "I am in control of my destiny, shaping my future with purpose.",
                "I am empowered to make choices that positively impact my life.",
                "I stay focused on my goals and committed to my personal growth.",
                "I am persistent, and I will never give up on what I believe in.",
                "Every experience is an opportunity for me to learn and grow.",
                "I am confident in my ability to overcome any challenge.",
                "I am resilient, rising each time I encounter a setback.",
                "I am motivated to make today a truly amazing day.",
                "I am capable of accomplishing anything I set my mind to.",
                "I am fully dedicated to my growth and future success.",
                "I am a powerful creator, designing my own reality.",
                "I am consistently moving forward toward my dreams.",
                "I am proud of the dedication and effort I put in each day.",
                "I am determined and will not be deterred from my goals.",
                "I am ready to take on new challenges and grow from them.",
                "My drive for success motivates me to reach new heights.",
                "I am focused on building a life I truly love.",
                "I am confident, capable, and determined to succeed.",
                "I am open to every opportunity that supports my growth.",
                "I am deserving of all the success I seek.",
                "I am inspired and motivated to become my best self.",
                "I am creating a future that aligns with my deepest desires.",
                "I am filled with excitement and energy as I work toward my goals.",
                "I am committed to transforming my dreams into reality.",
                "I am courageous, ready to take risks in pursuit of my dreams.",
                "I am destined for greatness, and I embrace it fully.",
                "I am worthy of every dream and goal that I pursue.",
                "I am relentless in my pursuit of success and joy.",
                "I am fully dedicated to achieving my dreams and goals.",
                "I am proud of myself for following my heart and aspirations.",
                "I am inspired to keep moving forward and making progress.",
                "I embrace each step of my journey with faith and optimism."
            ],
            "Gratitude": [
                "I am grateful for every experience that has shaped my journey.",
                "I appreciate the blessings in my life and welcome even more.",
                "I am thankful for the love of family, friends, and cherished ones.",
                "I am grateful for the beauty and serenity of nature around me.",
                "I find value in every challenge, thankful for each lesson learned.",
                "I am blessed to embrace each new day with gratitude and joy.",
                "I am thankful for the opportunities that unfold before me.",
                "I recognize and appreciate the abundance that surrounds me.",
                "I am grateful for my health and the strength it gives me.",
                "I feel deep gratitude for the love and care that others share with me.",
                "I am thankful for the kindness that fills my life.",
                "I honor the strength I’ve cultivated within myself and am grateful for it.",
                "I appreciate every positive influence that has enriched my path.",
                "I am grateful for my power to create meaningful change.",
                "I treasure the small moments that add beauty to my life.",
                "I am grateful for my unique purpose and journey.",
                "I am deeply thankful for the support I receive from those around me.",
                "I appreciate the comfort of my home and the nourishment in my life.",
                "I am grateful for each moment of joy that brightens my day.",
                "I am thankful for challenges that have strengthened my resilience.",
                "I embrace each chance to grow and become my best self.",
                "I see beauty in today and feel gratitude for its gifts.",
                "I am grateful for the light and warmth brought by those I love.",
                "I recognize the abundance in my life and give thanks for it.",
                "I am grateful for the wisdom that has blossomed over time.",
                "I cherish each moment of peace that fills my heart.",
                "I am thankful for my capacity to make a positive impact on others.",
                "I am grateful for the opportunity to give and receive love.",
                "I hold gratitude for my life and all it encompasses.",
                "I am thankful for every step that has led me to this moment.",
                "I honor and am grateful for my body, mind, and soul.",
                "I am grateful for the limitless opportunities around me.",
                "I give thanks for the resilience and inner strength within me.",
                "I appreciate every step along my path and the growth it brings.",
                "I am thankful for the steadfast support of friends and family.",
                "I treasure each breath as a gift of life.",
                "I embrace and appreciate the beauty of life’s offerings.",
                "I feel grateful for the preciousness of each moment.",
                "I am thankful for the guidance and wisdom that comes my way.",
                "I am empowered by my ability to create happiness in my life.",
                "I am grateful for the warmth of love and compassion.",
                "I acknowledge and am thankful for the abundance in my life.",
                "I appreciate every chance to learn, grow, and expand.",
                "I welcome each life lesson with a heart full of gratitude.",
                "I am thankful for the positive energy that surrounds me.",
                "I feel blessed for the love that flows into my life.",
                "I appreciate each act of kindness, however small.",
                "I am thankful for the chance to live a life of meaning and fulfillment.",
                "I am fully present and grateful for the beauty of now.",
                "I am thankful for every blessing, big and small, in my life."
            ],
            "Healing": [
                "I allow myself the time and space to fully heal.",
                "My healing journey is unique, and I honor each step I take.",
                "I am gentle with myself as I work through past hurts.",
                "I trust in my inner wisdom and the power of my spirit to guide me toward healing.",
                "Every day, I release old wounds and welcome fresh growth.",
                "I am deserving of inner peace and emotional freedom.",
                "I forgive myself, letting healing flow naturally within me.",
                "I am open to receiving the support I need for my healing.",
                "I let go of the past and focus on finding joy in the present.",
                "I am patient with myself and allow my heart the time it needs to heal.",
                "I trust that time, self-love, and patience will bring me peace.",
                "I embrace my feelings as essential steps in my healing journey.",
                "I release pain, opening my heart to love and happiness.",
                "I am resilient and capable of overcoming anything in my path.",
                "Healing takes time, and I am kind and compassionate with myself.",
                "I am grateful for every step forward in my healing journey.",
                "I am strong, courageous, and capable in the face of healing.",
                "I release guilt and shame, allowing space for healing and peace.",
                "I heal in my own way and at my own pace, with patience.",
                "I embrace the healing power of love within my soul.",
                "I let go of resentment, allowing forgiveness to flow through me.",
                "I am not defined by my past; I am creating a beautiful future.",
                "I am worthy of love, happiness, and a calm, peaceful mind.",
                "I release old hurts and open my heart to healing energies.",
                "I honor my emotions, allowing them to guide me toward wholeness.",
                "I am grateful for the strength that sustains me in my healing journey.",
                "Each day, I grow closer to a state of inner peace and wholeness.",
                "I trust in my heart’s wisdom to restore harmony within me.",
                "I am deserving of serenity, happiness, and inner calm.",
                "I let go of fear and embrace healing in all its forms.",
                "Forgiveness frees my heart, clearing the path for healing.",
                "I am worthy of a peaceful heart and a deeply healed spirit.",
                "I release what harms me, creating space for joy and peace.",
                "My heart is open to healing, love, and personal transformation.",
                "I am grateful for each step forward on my healing path.",
                "I allow myself to feel, heal, and grow from all experiences.",
                "I am free from the burdens of my past, welcoming a peaceful future.",
                "Healing is a journey, and I celebrate my progress each day.",
                "I trust the process of healing, even when it feels challenging.",
                "I am open to the love and support that aids my healing journey.",
                "I release all that no longer serves my mind and spirit.",
                "My heart is mending, and I am becoming whole again.",
                "I am grateful for my resilience and the strength to heal and grow.",
                "I embrace healing as a path to my most fulfilled self.",
                "I release negativity and welcome inner peace and balance.",
                "With each day, I grow stronger, wiser, and more at peace.",
                "I am a survivor, and my healing is a testament to my strength.",
                "I am learning to forgive and release for my own peace.",
                "I am worthy of a vibrant, joyful, and peaceful life.",
                "I am healing, evolving, and becoming the best version of myself."
            ],
            "Forgiveness": [
                "I forgive myself and others, freeing my heart from pain.",
                "Forgiveness brings peace to my soul, and I embrace it fully.",
                "I release resentment and choose forgiveness as my path.",
                "Forgiveness is a precious gift I offer to myself for inner peace.",
                "I am grateful for the freedom that forgiveness offers my heart.",
                "I forgive past mistakes, allowing myself space to grow.",
                "I let go of grudges, making room for love and compassion.",
                "I am capable of forgiving, healing, and moving forward in peace.",
                "Forgiveness allows me to release anger and find serenity.",
                "I am stronger than resentment and rise above bitterness.",
                "I release the past, forgiving everyone involved, including myself.",
                "Forgiveness brings me closer to inner peace and true joy.",
                "I accept my imperfections and forgive myself with compassion.",
                "I release hurt, embracing compassion and understanding instead.",
                "I am open to the transformative power of forgiveness.",
                "I choose forgiveness as a path to my own freedom.",
                "I forgive others, letting go of pain to find peace within myself.",
                "I am thankful for the calm and clarity that forgiveness brings.",
                "I forgive myself and celebrate my journey of growth and healing.",
                "Forgiveness opens my heart to love, peace, and harmony.",
                "I choose love and forgiveness over lingering anger or resentment.",
                "I let go of grudges, allowing inner peace to enter my life.",
                "I release all blame and forgive myself completely.",
                "Forgiveness is the bridge to a healthier, happier life.",
                "I consciously choose forgiveness, freeing myself from negativity.",
                "I let go of resentment and embrace the freedom of forgiveness.",
                "Forgiveness strengthens and heals me, bringing lasting peace.",
                "I am free from past pain through the act of forgiving.",
                "I am grateful for the peaceful heart that forgiveness brings.",
                "I forgive myself for clinging to past pain, choosing freedom instead.",
                "Forgiveness is a loving act I offer to myself and others.",
                "I am patient with myself as I learn and grow through forgiveness.",
                "I am capable of forgiving with grace and understanding.",
                "Forgiveness clears negativity from my heart, filling it with peace.",
                "I let go of resentment, allowing love and joy to fill its place.",
                "I forgive myself for what I did not know at the time.",
                "Forgiveness gives me strength and mastery over my emotions.",
                "I choose forgiveness to free myself from any lingering pain.",
                "I am grateful for the inner peace that forgiveness bestows upon me.",
                "I forgive my imperfections and embrace my journey toward growth.",
                "I release past hurt, stepping forward with peace and purpose.",
                "Forgiveness is my path to a joyful, brighter future.",
                "I am healing and growing stronger through each act of forgiveness.",
                "I am grateful for the lessons and liberation forgiveness provides.",
                "I forgive, let go, and move forward with love in my heart.",
                "Forgiveness allows me to release what I cannot change.",
                "I forgive others for my own peace, not just for their sake.",
                "Forgiveness clears my heart and mind of negativity.",
                "I am thankful for the profound inner peace that forgiveness brings.",
                "I forgive myself and others, welcoming peace, growth, and happiness.",
            ],
            "Mindfulness": [
                "I am fully present in this moment, aware and at peace.",
                "Today, I choose mindfulness and calm over worry and stress.",
                "I savor each moment, finding joy in the beauty of now.",
                "I release the urge to rush and embrace life’s natural pace.",
                "Each breath I take centers me and fills me with peace.",
                "I am at peace with myself and in harmony with my surroundings.",
                "I let go of the past and future, immersing fully in the present.",
                "I find joy in simple moments and appreciate life's small wonders.",
                "I am calm, centered, and fully engaged in this moment.",
                "I release judgment, approaching each experience with openness.",
                "I am grateful for the now, knowing this moment is all I need.",
                "I find inner peace by focusing on what truly matters to me.",
                "I am mindful of my thoughts, actions, and my place in the world.",
                "I am grounded in the present, open to all that it brings.",
                "Mindfulness is my pathway to lasting peace and happiness.",
                "I observe my thoughts, letting them flow without judgment.",
                "I am in harmony with life, moving with its natural rhythm.",
                "I let go of distractions, embracing the stillness of now.",
                "Each day, I cultivate a mindful, present state of being.",
                "I am fully engaged in this moment, free from distractions.",
                "I find serenity in simply witnessing life as it unfolds.",
                "I am aware, present, and fully alive in every experience.",
                "I release anxiety by grounding myself in the here and now.",
                "I embrace the gift of today, releasing concerns about tomorrow.",
                "With each breath, I find a sense of calm and clarity.",
                "I allow myself to experience this moment without judgment.",
                "I choose to be here, in this moment, where peace resides.",
                "I am grateful for each experience, trusting it serves my growth.",
                "I focus on what I can control, letting go of the rest.",
                "I find peace in nature’s beauty and the tranquility it brings.",
                "I am at ease, centered, and present within my body and mind.",
                "I find comfort and contentment in knowing this moment is enough.",
                "Mindfulness brings me closer to peace, joy, and purpose.",
                "I observe my emotions, letting them pass without control.",
                "I am grounded, centered, and calm in this present moment.",
                "I release the need to control, embracing life’s flow.",
                "Every day is a new opportunity to practice presence and awareness.",
                "I find balance in both stillness and gentle movement.",
                "I am deeply connected to this moment and all it offers.",
                "I let go of attachment to the past, embracing the present fully.",
                "Today, I choose to be mindful in both actions and words.",
                "I find peace by living fully in each precious moment.",
                "I am present, open, and engaged with the world around me.",
                "I am grateful for the peace and insight mindfulness brings.",
                "I am patient, present, and accepting of life exactly as it is.",
                "I observe my life with calm, acceptance, and an open heart.",
                "I let go of distractions, choosing to focus on the now.",
                "I am aware of the beauty in each moment, finding joy in it all.",
                "I welcome each experience with presence and gratitude.",
                "Mindfulness guides me to peace, joy, and a life filled with meaning.",
            ],
            "Abundance": [
                "I am a magnet for wealth, prosperity, and joyful abundance.",
                "Opportunities for growth and success surround me, and I confidently embrace them.",
                "I release all limiting beliefs and fully embrace abundance in all its forms.",
                "My bank account grows as I focus on my goals and dreams with gratitude.",
                "Money flows easily to me from various sources, and I receive it openly.",
                "Every day, I attract abundance into my life with a grateful heart.",
                "I am deserving of a life filled with prosperity, joy, and fulfillment.",
                "I align with the energy of wealth and welcome its presence in my life.",
                "Every action I take supports greater prosperity and financial freedom.",
                "I am thankful for the limitless flow of abundance that blesses my life.",
                "I am financially free, and I celebrate my growing prosperity.",
                "I am worthy of achieving all my financial goals and dreams.",
                "Money flows effortlessly to me as I pursue my purpose.",
                "The universe continually brings new wealth into my life.",
                "I welcome unexpected income and prosperity from many sources.",
                "I am capable of creating wealth, joy, and abundance in all areas.",
                "The money I attract brings positive change to my life and others.",
                "I am in the flow of prosperity, feeling joy and gratitude.",
                "Financial security and freedom are my birthrights, and I claim them now.",
                "I am open to all forms of wealth and abundance that life has to offer.",
                "Every day, I grow richer in wealth, health, and happiness.",
                "My income grows as I serve others and share my talents generously.",
                "The universe fully supports my financial success and well-being.",
                "By being my authentic self, I attract wealth and opportunities.",
                "I maintain an abundance mindset, welcoming limitless possibilities.",
                "I gratefully welcome a steady flow of money into my life.",
                "I have the power to create and enjoy financial freedom and peace.",
                "I am grateful for the money that flows to me effortlessly.",
                "My relationship with money is positive, and I attract prosperity.",
                "I am open to receiving an unlimited flow of abundance daily.",
                "Abundance flows into all aspects of my life—health, love, and joy.",
                "I am surrounded by love, kindness, and fulfilling relationships.",
                "I welcome vibrant health that nourishes my mind, body, and spirit.",
                "Each day, my heart opens to greater love and lasting connections.",
                "I am grateful for the opportunities that bring growth to my career.",
                "Abundance is my natural state, filling my life with success and peace.",
                "I am worthy of vibrant health, and I welcome vitality into my life.",
                "Love flows freely to and from me, enriching all my relationships.",
                "I embrace opportunities that align with my purpose and joy.",
                "Prosperity fills every corner of my life, bringing peace and fulfillment.",
                "My life is enriched with meaningful connections and boundless love.",
                "I am open to blessings in all forms, from wealth to well-being.",
                "My career flourishes as I share my talents with the world.",
                "Abundant energy fills me, supporting my health and spirit.",
                "Love and harmony uplift my relationships, creating joy and inspiration.",
                "I attract meaningful experiences that help me grow and thrive.",
                "I am surrounded by supportive people who bring joy to my life.",
                "My life overflows with love, beauty, and peace in all its forms.",
                "I welcome health, wealth, wisdom, and happiness as natural parts of my journey.",
                "I am blessed with good health, filling me with energy and vitality.",
                "I attract enriching relationships that foster growth and joy.",
                "Prosperity flows easily into my life, enhancing my career, health, and relationships.",
                "My relationships radiate love, kindness, and mutual respect.",
                "I am open to the endless flow of health, wealth, and happiness around me.",
                "Abundance in love, joy, and success flows naturally into my life.",
            ],
            "Growth and Transformation": [
                "I embrace change as an opportunity to grow and transform.",
                "I am evolving every day into the best version of myself.",
                "Every challenge I face becomes a steppingstone toward growth.",
                "I am open to transformation and welcome positive changes in my life.",
                "Growth is a journey, and I am grateful for each step I take.",
                "I am capable of achieving more than I ever imagined.",
                "I release the past and welcome the future with confidence.",
                "I grow stronger, wiser, and more resilient with each passing day.",
                "Every experience I encounter helps me become better and wiser.",
                "I trust the process of transformation and embrace it fully.",
                "I am open to new possibilities and welcome opportunities for growth.",
                "I am grateful for the lessons that shape me and help me evolve.",
                "I let go of fear and welcome growth with an open heart.",
                "Transformation brings me closer to my true and authentic self.",
                "I am a work in progress, continuously learning and improving.",
                "Growth begins with self-reflection and understanding who I am.",
                "The journey to self-love is worth every step, embracing both flaws and strengths.",
                "Letting go makes room for something greater; I trust what’s meant for me.",
                "Releasing what doesn’t serve me creates space for peace and fulfillment.",
                "I am patient with myself as I grow and transform at my own pace.",
                "Every day, I align more closely with my purpose.",
                "I let go of limiting beliefs and step into my full potential.",
                "Growth happens outside my comfort zone, and I am ready to explore.",
                "I focus on progress rather than perfection.",
                "I honor my unique path and celebrate my journey.",
                "I release what no longer serves me, opening space for what will.",
                "I am deserving of all the growth and success I envision.",
                "True transformation begins within, and I am open to inner change.",
                "Changing my mindset empowers me to change my life.",
                "I trust myself and the journey I am on.",
                "Each day offers a fresh opportunity to learn, grow, and evolve.",
                "I release doubt and step into the possibility of greatness.",
                "I approach transformation with courage and confidence.",
                "My past does not define me; I am creating a new future.",
                "I am resilient, rising above challenges with strength and grace.",
                "I move forward, letting go of what lies behind.",
                "Every lesson learned propels me forward on my journey.",
                "I am constantly becoming a better version of myself.",
                "I embrace change with courage and optimism.",
                "I honor my growth as a beautiful gift and blessing.",
                "Transformation is ongoing, and I welcome it every day.",
                "I am worthy of all the wonderful growth life has to offer.",
                "I see obstacles as steppingstones for expansion.",
                "Every experience is shaping me into who I am meant to be.",
                "I am open to seeing the world in new and different ways.",
                "I embrace the person I am becoming for my highest good.",
                "Each small step I take contributes to profound transformation.",
                "I am a continuous work in progress, evolving with purpose.",
                "I welcome change as a natural part of my life journey.",
                "Each transformation brings me closer to my truest self."
            ],
            "Fear": [
                "I trust that everything will unfold as it should. I am ready for this.",
                "Life may be tough, but I am tougher.",
                "True courage emerges when I face what frightens me.",
                "When I fuel my dreams instead of my fears, miracles happen.",
                "Even in fear, I achieve extraordinary things.",
                "A fresh start awaits, and I trust in the magic of new beginnings.",
                "Every step I take builds my courage and strength.",
                "What good are wings without the courage to fly?",
                "Growth begins the moment I step beyond my comfort zone.",
                "Here’s a reminder: everything will be okay in the end.",
                "I am brave enough to venture into the unknown.",
                "I am capable of doing hard things.",
                "Better to say 'Oops!' than to regret a 'What if?'",
                "Everything I seek is just beyond my fear.",
                "When I face fear directly, it starts to dissolve.",
                "I am braver than I believe and more loved than I realize.",
                "I grow from every challenge I encounter.",
                "If it costs my peace, it’s too expensive.",
                "It’s okay to feel happy, healing, and hurting all at once.",
                "I allow myself to feel deeply so that healing can begin.",
                "Today, I choose not to stress over things I can’t control.",
                "I leave the past behind, stepping forward with clarity.",
                "Some storms don’t disrupt—they clear the path ahead.",
                "The step I fear most may be the one that changes everything.",
                "When I confront fear, it loses its power.",
                "What if I fall? But oh, what if I soar?",
                "My life expands with every risk I dare to take.",
                "Fate favors the fearless.",
                "Fear may whisper, but my spirit roars.",
                "I embrace the unknown, where possibility thrives.",
                "With each challenge, my courage grows stronger.",
                "Fear is a visitor; courage is my home.",
                "I walk into the unknown with my heart open.",
                "Fear is brief, but the strength it brings lasts.",
                "I am stronger than the doubts that arise in my mind.",
                "A fearless heart has no limits.",
                "Fear fades, but regret is lifelong.",
                "Where there is fear, there is power waiting to be claimed.",
                "I hold the key to breaking free from my own limitations. With courage, I open doors to endless possibilities.",
                "I trust myself to leap, leaving fear behind.",
                "I have the power to rewrite my story with courage.",
                "Each act of courage transforms my path forward.",
                "I rise above the whispers of doubt within.",
                "Every fear I face builds my confidence.",
                "In every shadow lies a light ready to shine.",
                "I embrace my strength and release what holds me back.",
                "I am my greatest source of courage.",
                "I dare to step into the unknown, where magic lives.",
                "My spirit knows no limits when I am fearless.",
                "I let my dreams overshadow my fears."
            ],
            "Health": [
                "I am grateful for my body and its ability to heal and thrive.",
                "Every cell in my body is filled with energy, health, and vitality.",
                "I nourish my body with healthy choices, and it thanks me with wellness.",
                "I am in tune with my body’s needs, and I honor them each day.",
                "My mind, body, and soul are in harmony, radiating vibrant health.",
                "I am worthy of good health and feel it in every part of me.",
                "I listen to my body’s wisdom and care for it with love.",
                "I release all tension, inviting peace and wellness into my body.",
                "Every day, my health improves and my energy increases.",
                "I am grateful for the gift of a strong, healthy body.",
                "I choose habits that nourish my body, mind, and spirit.",
                "With each breath, I am filled with healing energy.",
                "I trust in my body’s natural ability to heal and restore.",
                "I am dedicated to maintaining my health and well-being.",
                "I embrace a lifestyle that supports my health and happiness.",
                "I am kind and patient with myself as I strive for wellness.",
                "Every day, I make choices that bring me closer to optimal health.",
                "My body is my sanctuary, and I honor it with respect and care.",
                "I love my body and treat it with the care it deserves.",
                "I am surrounded by health and well-being in every area of my life.",
                "I am grateful for a mind that is calm and a body that is strong.",
                "I allow my body to rest, heal, and renew with ease.",
                "I fill my mind with positive thoughts that support my health.",
                "I let go of habits that no longer serve my highest good.",
                "I feel strong, capable, and healthy in body, mind, and spirit.",
                "I release stress and invite calmness into my life.",
                "My body deserves to be healthy, and I nourish it with kindness.",
                "I am energized, healthy, and grateful for each day.",
                "I let go of worry and trust in my body’s ability to thrive.",
                "Every choice I make supports my journey to vibrant health.",
                "I am patient and gentle with myself on my health journey.",
                "I am grateful for a body that serves me well each day.",
                "I nourish my mind and body with positive, healing energy.",
                "I am in balance, and my body is a reflection of my well-being.",
                "I feel light, energized, and full of vitality.",
                "I take care of my body with gratitude, and it rewards me with health.",
                "Every part of my body feels relaxed, healthy, and at peace.",
                "I am grateful for the health, energy, and strength within me.",
                "I release old patterns and embrace habits that support my health.",
                "I am grateful for a healthy body that allows me to live fully.",
                "My health journey is unique, and I honor my progress each day.",
                "I trust in my ability to make choices that support my wellness.",
                "I fill my life with nourishing relationships and experiences.",
                "My immune system is strong, and I feel well-protected and safe.",
                "I am thankful for the energy and vitality I feel each day.",
                "I am committed to a life of wellness, balance, and joy.",
                "I feel balanced, healthy, and connected to my body’s wisdom.",
                "I celebrate every small step forward on my health journey.",
                "I am grateful for the strength that my body provides me.",
                "I welcome vibrant health, energy, and wellness into my life each day."
            ]
        }
        self.displayed_affirmations = self.load_displayed_affirmations()

    def load_displayed_affirmations(self):
        # Load the displayed affirmations from a JSON file if it exists
        try:
            with open("displayed_affirmations.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            # If the file doesn't exist, initialize with empty lists
            return {category: [] for category in self.categories}

    def save_displayed_affirmations(self):
        # Save the displayed affirmations to a JSON file
        with open("displayed_affirmations.json", "w") as f:
            json.dump(self.displayed_affirmations, f)
    
    def get_affirmation(self, category=None):
        if category:
            affirmations = [
                a for a in self.categories[category]
                if a not in self.displayed_affirmations.get(category, [])
            ]
            if not affirmations:
                # Reset category if all affirmations have been shown
                self.displayed_affirmations[category] = []
                affirmations = self.categories[category]
            affirmation = random.choice(affirmations)
            self.displayed_affirmations[category].append(affirmation)
        else:
            # Collect all affirmations across categories
            all_affirmations = [
                a for aff_list in self.categories.values() for a in aff_list
            ]
            displayed_all = [
                a for aff_list in self.displayed_affirmations.values() for a in aff_list
            ]
            affirmations = [a for a in all_affirmations if a not in displayed_all]
            if not affirmations:
                # Reset all categories if all affirmations have been shown
                self.displayed_affirmations = {category: [] for category in self.categories}
                affirmations = all_affirmations
            affirmation = random.choice(affirmations)
            # Add affirmation to the respective category in displayed list
            for cat, aff_list in self.categories.items():
                if affirmation in aff_list:
                    self.displayed_affirmations.setdefault(cat, []).append(affirmation)
                    break

        self.save_displayed_affirmations()
        return affirmation

class AffirmationApp:
    def __init__(self):
        self.generator = AffirmationGenerator()

    def display_welcome_message(self):
        print("♥" * 50)
        print("♥                                                ♥")
        print("♥        💖 Welcome to Your Daily Dose 💖        ♥")
        print("♥        💖  of Inspiration and Magic  💖        ♥")
        print("♥                                                ♥")
        print("♥" * 50)
        print("\nEmbrace each day with positivity, gratitude, and courage.")
        print("Let's uncover an affirmation that speaks to your soul.\n")

    def prompt_user_choice(self):
        print("\n✨ Would you like a random affirmation or choose a category?✨")
        print("1. 🌀 Random Affirmation")
        print("2. 🌈 Choose a Category")
        return input("Enter 1 for Random or 2 for Category: ")

    def choose_category(self):
        print("\nAvailable Categories:")
        categories = list(self.generator.categories.keys())
        idx = 1  # Start counter for display
        for category in categories:
            print(f"{idx}. {category}")
            idx += 1

        category_index = input("Choose a category by entering the number: ")
        if category_index.isdigit():
            category_index = int(category_index) - 1
            if 0 <= category_index < len(categories):
                return categories[category_index]
            else:
                print("Invalid choice. Please enter a number within the range.")
        else:
            print("Invalid input. Please enter a valid number.")
        return None

    def run(self):
        self.display_welcome_message()
        # Loop to keep asking for input until a valid choice is made
        while True:
            choice = self.prompt_user_choice()
            if choice == "1":
                affirmation = self.generator.get_affirmation()
                print(f'\n"{affirmation}"')
            elif choice == "2":
                category = self.choose_category()
                if category:
                    affirmation = self.generator.get_affirmation(category)
                    print(f'\n"{affirmation}"')
            else:
                print("Invalid choice. Please enter 1 for Random or 2 for Category.")

# Run the app
if __name__ == "__main__":
    app = AffirmationApp()
    app.run()