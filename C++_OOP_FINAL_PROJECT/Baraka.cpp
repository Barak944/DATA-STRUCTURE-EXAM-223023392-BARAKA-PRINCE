#include <iostream>
using namespace std;

// --------- 1. Define Date Struct ---------
struct Date {
    int day, month, year;
};

// --------- 2. Function to compute days between dates ---------
int computeDays(const Date* start, const Date* end) {
    // Simplified calculation: assumes 30 days per month and 360 days per year
    int startTotal = start->day + start->month * 30 + start->year * 360;
    int endTotal = end->day + end->month * 30 + end->year * 360;
    return endTotal - startTotal;
}

// --------- 3. Abstract Class Vehicle ---------
class Vehicle {
public:
    virtual float calcRent(const Date* start, const Date* end) = 0;
    virtual ~Vehicle() {}
};

// --------- 4. Derived Class: Car ---------
class Car : public Vehicle {
    float dailyRate;
public:
    Car(float rate) : dailyRate(rate) {}
    float calcRent(const Date* start, const Date* end) override {
        int days = computeDays(start, end);
        return dailyRate * days;
    }
};

// --------- 5. Derived Class: Truck ---------
class Truck : public Vehicle {
    float flatRate, payloadSurcharge;
public:
    Truck(float rate, float surcharge)
        : flatRate(rate), payloadSurcharge(surcharge) {}

    float calcRent(const Date* start, const Date* end) override {
        int days = computeDays(start, end);
        return flatRate + (payloadSurcharge * days);
    }
};

// --------- 6. Add and Remove Vehicle Functions ---------
void addVehicle(Vehicle**& inventory, int& size, Vehicle* v) {
    Vehicle** newInventory = new Vehicle*[size + 1];
    for (int i = 0; i < size; ++i)
        newInventory[i] = inventory[i];
    newInventory[size] = v;
    delete[] inventory;
    inventory = newInventory;
    ++size;
}

void removeVehicle(Vehicle**& inventory, int& size, int index) {
    if (index < 0 || index >= size) return;
    Vehicle** newInventory = new Vehicle*[size - 1];
    for (int i = 0, j = 0; i < size; ++i)
        if (i != index)
            newInventory[j++] = inventory[i];
    delete[] inventory;
    inventory = newInventory;
    --size;
}

// --------- 7. Main Function ---------
int main() {
    int size = 0;
    Vehicle** inventory = NULL;

    // Allocate and add vehicles
    addVehicle(inventory, size, new Car(40.0f));           // Car: $40 per day
    addVehicle(inventory, size, new Truck(100.0f, 25.0f)); // Truck: $100 + $25/day

    // Allocate rental dates
    Date* d1 = new Date{1, 6, 2025};
    Date* d2 = new Date{6, 6, 2025};

    // Calculate and display rent
    for (int i = 0; i < size; ++i) {
        float rent = inventory[i]->calcRent(d1, d2);
        cout << "Vehicle " << i << " rent: $" << rent << endl;
    }

    // Remove the first vehicle
    removeVehicle(inventory, size, 0);

    cout << "\nAfter removing vehicle 0:\n";
    for (int i = 0; i < size; ++i) {
        float rent = inventory[i]->calcRent(d1, d2);
        cout << "Vehicle " << i << " rent: $" << rent << endl;
    }

    // Cleanup
    for (int i = 0; i < size; ++i)
        delete inventory[i];
    delete[] inventory;
    delete d1;
    delete d2;

    return 0;
}

