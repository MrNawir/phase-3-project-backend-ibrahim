"""
Seed script to populate the database with Kenyan venue and event data.
Run with: python seed.py
"""
from datetime import date, time
from app.database import SessionLocal, engine, Base
from app.models import Venue, Event, Ticket

# Create tables
Base.metadata.create_all(bind=engine)


def seed_database():
    db = SessionLocal()

    try:
        # Clear existing data
        db.query(Ticket).delete()
        db.query(Event).delete()
        db.query(Venue).delete()
        db.commit()

        # Create 10 Kenyan Venues with images
        venues = [
            Venue(
                name="Kasarani Stadium (Moi International Sports Centre)",
                address="Thika Road, Kasarani",
                city="Nairobi",
                capacity=60000,
                image_url="https://images.unsplash.com/photo-1577223625816-7546f13df25d?w=800"  # Large stadium
            ),
            Venue(
                name="Nyayo National Stadium",
                address="Mombasa Road, near CBD",
                city="Nairobi",
                capacity=30000,
                image_url="https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800"  # Football stadium
            ),
            Venue(
                name="Nairobi City Stadium",
                address="Jogoo Road",
                city="Nairobi",
                capacity=15000,
                image_url="https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800"  # Sports field
            ),
            Venue(
                name="KICC (Kenyatta International Convention Centre)",
                address="City Square, Harambee Avenue",
                city="Nairobi",
                capacity=4000,
                image_url="https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=800"  # Convention center
            ),
            Venue(
                name="Uhuru Gardens National Monument",
                address="Langata Road",
                city="Nairobi",
                capacity=50000,
                image_url="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800"  # Park/gardens
            ),
            Venue(
                name="The Carnivore",
                address="Langata Road, near Wilson Airport",
                city="Nairobi",
                capacity=10000,
                image_url="https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=800"  # Concert venue
            ),
            Venue(
                name="Kasarani Indoor Arena",
                address="Moi International Sports Centre, Thika Road",
                city="Nairobi",
                capacity=5000,
                image_url="https://images.unsplash.com/photo-1504450758481-7338eba7524a?w=800"  # Indoor arena
            ),
            Venue(
                name="Two Rivers Mall Arena",
                address="Limuru Road, Runda",
                city="Nairobi",
                capacity=3000,
                image_url="https://images.unsplash.com/photo-1567521464027-f127ff144326?w=800"  # Mall/modern venue
            ),
            Venue(
                name="Kipchoge Keino Stadium",
                address="Eldoret Town",
                city="Eldoret",
                capacity=10000,
                image_url="https://images.unsplash.com/photo-1587280501635-68a0e82cd5ff?w=800"  # Athletics track
            ),
            Venue(
                name="Mombasa Municipal Stadium",
                address="Mombasa Island",
                city="Mombasa",
                capacity=12000,
                image_url="https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=800"  # Coastal stadium
            ),
        ]

        for venue in venues:
            db.add(venue)
        db.commit()

        print(f"✓ Created {len(venues)} venues")

        # Refresh to get IDs
        for venue in venues:
            db.refresh(venue)

        # Create 15 Kenyan Events
        events = [
            # SPORTS - Football (6 events)
            Event(
                venue_id=venues[1].id,  # Nyayo Stadium
                title="Mashemeji Derby: Gor Mahia vs AFC Leopards",
                description="Kenya's biggest football rivalry! The historic Mashemeji Derby between arch-rivals Gor Mahia (K'Ogalo) and AFC Leopards (Ingwe). Experience the passion as the green and white of Gor Mahia clash with the blue and white of AFC Leopards in this FKF Premier League showdown. This rivalry dates back to 1968 and remains the most attended fixture in Kenyan football.",
                category="Sports",
                event_date=date(2025, 3, 15),
                event_time=time(15, 0),
                image_url="https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=800"  # Soccer match
            ),
            Event(
                venue_id=venues[0].id,  # Kasarani
                title="Harambee Stars vs Uganda Cranes - AFCON Qualifier",
                description="Kenya's national football team, Harambee Stars, faces East African rivals Uganda Cranes in a crucial Africa Cup of Nations qualifier at Kasarani Stadium. Come support the national team as they battle for continental glory! The East African derby is always a fiercely contested match with national pride on the line.",
                category="Sports",
                event_date=date(2025, 6, 8),
                event_time=time(16, 0),
                image_url="https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?w=800"  # Football stadium
            ),
            Event(
                venue_id=venues[2].id,  # City Stadium
                title="FKF Premier League: Tusker FC vs Kakamega Homeboyz",
                description="Top-flight Kenyan Premier League action as defending champions Tusker FC host Kakamega Homeboyz at Nairobi City Stadium. Watch the brewers defend their title against the determined Western Kenya outfit in this exciting league fixture.",
                category="Sports",
                event_date=date(2025, 4, 20),
                event_time=time(15, 0),
                image_url="https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800"  # Soccer players
            ),
            Event(
                venue_id=venues[0].id,  # Kasarani
                title="Safari Sevens 2025",
                description="East Africa's premier rugby sevens tournament returns to Kasarani! Watch Kenya Shujaa and international teams from around the world battle it out in this exciting two-day rugby festival. The Safari Sevens has been running since 1996 and attracts top rugby nations.",
                category="Sports",
                event_date=date(2025, 10, 18),
                event_time=time(9, 0),
                image_url="https://images.unsplash.com/photo-1544131750-fa7e77d3ae59?w=800"
            ),
            Event(
                venue_id=venues[6].id,  # Kasarani Indoor
                title="KBF Basketball Finals",
                description="Watch the Kenya Basketball Federation Premier League Finals as Kenya's top basketball teams battle for the championship at the Kasarani Indoor Arena! Experience the best of Kenyan basketball talent competing for the ultimate prize.",
                category="Sports",
                event_date=date(2025, 5, 24),
                event_time=time(14, 0),
                image_url="https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800"
            ),
            Event(
                venue_id=venues[8].id,  # Kipchoge Keino Stadium
                title="Kip Keino Classic 2025",
                description="World Athletics Continental Tour Gold meeting featuring Kenya's world-class athletes competing against international stars in the home of champions! Named after legendary Olympian Kipchoge Keino, this event showcases the best of Kenyan athletics excellence.",
                category="Sports",
                event_date=date(2025, 5, 10),
                event_time=time(14, 0),
                image_url="https://images.unsplash.com/photo-1552674605-db6ffd4facb5?w=800"
            ),
            # CONCERTS (4 events)
            Event(
                venue_id=venues[4].id,  # Uhuru Gardens
                title="Sol Fest 2025 - Sauti Sol Reunion",
                description="Kenya's legendary afro-pop band Sauti Sol reunites for an epic concert at Uhuru Gardens! Featuring Bien, Savara, Chimano, and Polycarp performing their greatest hits including 'Midnight Train', 'Suzanna', 'Extravaganza', 'Short N Sweet', and 'Melanin'. A once-in-a-lifetime musical experience!",
                category="Concert",
                event_date=date(2025, 12, 21),
                event_time=time(18, 0),
                image_url="https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=800"
            ),
            Event(
                venue_id=venues[5].id,  # Carnivore
                title="Nyashinski Live at Carnivore",
                description="Kenyan hip-hop legend Nyashinski (formerly of Kleptomaniax) performs live at the iconic Carnivore! Experience hits like 'Mungu Pekee', 'Finyo', 'Malaika', 'Now You Know', and 'Hayawani' from Kenya's most celebrated rapper and performer.",
                category="Concert",
                event_date=date(2025, 8, 16),
                event_time=time(19, 0),
                image_url="https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=800"
            ),
            Event(
                venue_id=venues[5].id,  # Carnivore
                title="Bensoul & Nviiri Live",
                description="Sol Generation artists Bensoul and Nviiri the Storyteller bring their unique blend of Kenyan soul and R&B to the Carnivore stage. A night of smooth melodies, African rhythms, and storytelling through music. Expect performances of 'Nairobi', 'Pombe Sigara', and more!",
                category="Concert",
                event_date=date(2025, 7, 12),
                event_time=time(20, 0),
                image_url="https://images.unsplash.com/photo-1501612780327-45045538702b?w=800"
            ),
            Event(
                venue_id=venues[0].id,  # Kasarani
                title="Davido Live in Nairobi",
                description="Nigerian Afrobeats superstar Davido brings his electrifying performance to Kenya! Experience hits like 'Fall', 'If', 'Jowo', 'Unavailable', and 'Feel' live at Kasarani Stadium. The OBO (Omo Baba Olowo) delivers an unforgettable night of African music.",
                category="Concert",
                event_date=date(2025, 8, 30),
                event_time=time(18, 0),
                image_url="https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3?w=800"
            ),
            # COMEDY (2 events)
            Event(
                venue_id=venues[3].id,  # KICC
                title="Churchill Show Live Recording",
                description="Be part of Kenya's most popular comedy show! Churchill (Daniel Ndambuki) hosts a star-studded lineup of Kenya's finest comedians for a live TV recording at KICC. Featuring the best of Kenyan humor, skits, and surprise celebrity guests. Laugh till your ribs hurt!",
                category="Comedy",
                event_date=date(2025, 5, 3),
                event_time=time(19, 30),
                image_url="https://images.unsplash.com/photo-1527224538127-2104bb71c51b?w=800"
            ),
            Event(
                venue_id=venues[7].id,  # Two Rivers
                title="Eric Omondi: Night of a Thousand Laughs",
                description="Kenya's king of comedy Eric Omondi brings his hilarious stand-up special to Two Rivers! Get ready for non-stop laughter with Kenya's most viral comedian, known for his witty observations, celebrity impressions, and social commentary that has made him a household name.",
                category="Comedy",
                event_date=date(2025, 4, 5),
                event_time=time(20, 0),
                image_url="https://images.unsplash.com/photo-1585699324551-f6c309eedeca?w=800"
            ),
            # FESTIVALS (2 events)
            Event(
                venue_id=venues[4].id,  # Uhuru Gardens
                title="Koroga Festival 2025",
                description="East Africa's premier music and food festival returns to Uhuru Gardens! Three days of live performances from top African artists, gourmet food from Kenya's best chefs, art installations, and the best of African culture. A celebration of music, food, and community.",
                category="Festival",
                event_date=date(2025, 9, 13),
                event_time=time(12, 0),
                image_url="https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?w=800"
            ),
            Event(
                venue_id=venues[3].id,  # KICC
                title="Nairobi Fashion Week 2025",
                description="Kenya's premier fashion event showcasing the best of African design at the iconic KICC. Watch top Kenyan and African designers present their latest collections on the runway. A celebration of African creativity, style, and the continent's growing fashion industry.",
                category="Festival",
                event_date=date(2025, 11, 8),
                event_time=time(17, 0),
                image_url="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800"
            ),
        ]

        for event in events:
            db.add(event)
        db.commit()

        print(f"✓ Created {len(events)} events")

        # Refresh to get IDs
        for event in events:
            db.refresh(event)

        # Create 6 sample tickets with Kenyan names
        tickets = [
            Ticket(
                event_id=events[0].id,  # Mashemeji Derby
                buyer_name="James Ochieng",
                buyer_email="james.ochieng@email.co.ke",
                ticket_type="VIP",
                price=2500.00
            ),
            Ticket(
                event_id=events[0].id,  # Mashemeji Derby
                buyer_name="Mary Wanjiku",
                buyer_email="mary.wanjiku@email.co.ke",
                ticket_type="Standard",
                price=500.00
            ),
            Ticket(
                event_id=events[6].id,  # Sol Fest
                buyer_name="Brian Mwangi",
                buyer_email="brian.mwangi@email.co.ke",
                ticket_type="VIP",
                price=10000.00
            ),
            Ticket(
                event_id=events[6].id,  # Sol Fest
                buyer_name="Grace Akinyi",
                buyer_email="grace.akinyi@email.co.ke",
                ticket_type="Standard",
                price=2000.00
            ),
            Ticket(
                event_id=events[10].id,  # Churchill Show
                buyer_name="Peter Kamau",
                buyer_email="peter.kamau@email.co.ke",
                ticket_type="Standard",
                price=1500.00
            ),
            Ticket(
                event_id=events[9].id,  # Davido Live
                buyer_name="Faith Njeri",
                buyer_email="faith.njeri@email.co.ke",
                ticket_type="Premium",
                price=8000.00
            ),
        ]

        for ticket in tickets:
            db.add(ticket)
        db.commit()

        print(f"✓ Created {len(tickets)} tickets")
        print("\n🎉 Database seeded successfully with Kenyan venues and events!")

    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
